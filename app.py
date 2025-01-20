import asyncio
import random
import json
from telethon import TelegramClient
from telethon.tl.types import PeerChat, PeerChannel

accounts = [
    {"session": "account1", "api_id": {api_id}, "api_hash": "{api_hash}", "phone_number": "{phone_number}"},
    {"session": "account2", "api_id": {api_id}, "api_hash": "{api_hash}", "phone_number": "{phone_number}"},
    {"session": "account3", "api_id": {api_id}, "api_hash": "{api_hash}", "phone_number": "{phone_number}"},
    {"session": "account4", "api_id": {api_id}, "api_hash": "{api_hash}", "phone_number": "{phone_number}"},
]

target_group_username = "{chat_id}"

clients = []

def load_txt_file(file_name):

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.readlines()
    except Exception as e:
        print(f"Error loading file {file_name}: {e}")
        return []

def load_json_file(file_name):

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading file {file_name}: {e}")
        return []

async def process_messages(file_choice, target_group):
    if file_choice == 1:
        messages = load_txt_file('1.txt')
    elif file_choice == 2:
        messages = load_txt_file('2.txt')
    elif file_choice == 3:
        qa_data = load_json_file('3.json')

    while True:
        if file_choice in [1, 2]:
            for client in clients:
                message = random.choice(messages).strip()
                try:
                    print(f"Bot (Sending from {client.session.filename}, API ID: {client.api_id}): {message}")
                    await client.send_message(target_group, message)
                except Exception as e:
                    print(f"Error sending message: {e}")

                # Message send time, random between 1 and 3 seconds
                await asyncio.sleep(random.uniform(1, 3))

        elif file_choice == 3:
            for qa in qa_data:
                question = qa.get("question")
                answers = qa.get("answers", [])

                if not question or len(answers) < 2:
                    continue

                client_asking = random.choice(clients)
                other_clients = [client for client in clients if client != client_asking]

                if len(other_clients) < 2:
                    print("Not enough clients for responses. Skipping this Q&A.")
                    continue

                client_responding_1 = random.choice(other_clients)
                client_responding_2 = random.choice([client for client in other_clients if client != client_responding_1])

                try:
                    print(f"Bot (Asking from {client_asking.session.filename}, API ID: {client_asking.api_id}): {question}")
                    await client_asking.send_message(target_group, question)
                except Exception as e:
                    print(f"Error sending question: {e}")

                remaining_answers = list(answers)
                answer_1 = random.choice(remaining_answers)
                remaining_answers.remove(answer_1)
                answer_2 = random.choice(remaining_answers)

                try:
                    await asyncio.sleep(random.uniform(2, 5))
                    print(f"Bot (Responding from {client_responding_1.session.filename}, API ID: {client_responding_1.api_id}): {answer_1}")
                    await client_responding_1.send_message(target_group, answer_1)
                except Exception as e:
                    print(f"Error sending first answer: {e}")

                try:
                    await asyncio.sleep(random.uniform(2, 5))
                    print(f"Bot (Responding from {client_responding_2.session.filename}, API ID: {client_responding_2.api_id}): {answer_2}")
                    await client_responding_2.send_message(target_group, answer_2)
                except Exception as e:
                    print(f"Error sending second answer: {e}")

                await asyncio.sleep(random.uniform(2, 5))

async def start_clients():

    tasks = []
    for account in accounts:
        client = TelegramClient(account["session"], account["api_id"], account["api_hash"])
        tasks.append(client.start(phone=account["phone_number"]))
        clients.append(client)

    await asyncio.gather(*tasks)
    if len(clients) < 2:
        print("Not enough clients started. At least 2 clients are required.")
        return False

    return True

async def get_group_id(client, group_username):

    try:
        entity = await client.get_entity(group_username)
        if isinstance(entity, PeerChat):
            return entity.chat_id
        elif isinstance(entity, PeerChannel):
            return entity.channel_id
    except Exception as e:
        print(f"Error fetching group ID: {e}")
    return None

async def main():
    try:
        file_choice = int(input("Choose a file (1 for 1.txt, 2 for 2.txt, 3 for 3.json): "))
        if file_choice not in [1, 2, 3]:
            print("Invalid choice. Please select 1, 2, or 3.")
            return

        if not await start_clients():
            return

        print("Bots started listening for messages.")

        target_group_id = {target_group_id}
        print(f"Target Group ID: {target_group_id}")

        await process_messages(file_choice, target_group_id)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        for client in clients:
            await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
