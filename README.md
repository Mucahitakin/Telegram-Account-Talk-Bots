## Telegram Bot Automator

This project is written to automate sending messages to a specific Telegram group channel using multiple Telegram accounts. Users can select messages from different files, and the time between each message is randomly adjusted. Additionally, a question-and-answer format can be used to create interactive conversations in Telegram groups.

Features
	•	Support for Multiple Telegram Accounts: You can operate with multiple Telegram accounts at once.
	•	Message Sending: Messages can be sent automatically to a group channel from text files or JSON files.
	•	Randomized Message Sending Times: The time between messages is randomized, so the bots work in a more natural way.
	•	Question-Answer Format: Interactive conversations can be generated from questions and answers provided in a JSON file.
	•	Dynamic Group Targeting: The target group is dynamically selected via the chat_id (group ID) provided by the user.

Installation

Requirements
	•	Python 3.x
	•	Telethon library
	•	To install Telethon, you can use the following command:

```
pip install telethon

```


Configuration
	1.	API Key and Account Information:
	•	To get your Telegram API information, go to Telegram Developer Portal.
	•	Obtain the API ID and API hash, and place them into the accounts list in the script. You will also need to provide the session, api_id, api_hash, and phone_number for each account.

Example:

```
accounts = [
    {"session": "account1", "api_id": "your_api_id", "api_hash": "your_api_hash", "phone_number": "phone_number"},
    {"session": "account2", "api_id": "your_api_id", "api_hash": "your_api_hash", "phone_number": "phone_number"},
]
```


	2.	Prepare the Message Files:
	•	Messages are taken from 1.txt, 2.txt, or 3.json. The content of these files should be formatted as follows:
	•	1.txt and 2.txt: A plain text file where each line represents a message.
	•	3.json: A JSON file containing questions and answers.

 ```
Example of 3.json:

[
    {
        "question": "What is your favorite color?",
        "answers": ["Blue", "Red", "Green"]
    },
    {
        "question": "Where are you from?",
        "answers": ["New York", "London", "Paris"]
    }
]
```


	3.	Target Group:
	•	Messages will be sent to the group specified by target_group_username. This should be the username of the target group.
	•	The group ID (chat_id) is dynamically fetched using the Telegram API, so make sure to provide the correct chat_id value for the target group.

Usage
	1.	File Selection:
	•	When the program runs, it prompts the user to choose a file from which to send messages. The options are:
	•	1 for 1.txt
	•	2 for 2.txt
	•	3 for 3.json
	2.	Running the Bots:
	•	The program will start the bots and send messages to the selected target group. The messages will be sent with random intervals between them.
	3.	Message Sending:
	•	The messages from the selected file are sent to the target group. If 3.json is selected, questions and answers will be sent interactively.
	4.	Running the Program:
	•	To run the program, use the following command:

python bot.py



Code Explanation

Main Functions
	•	load_txt_file(file_name): Reads messages from the given .txt file and returns them as a list.
	•	load_json_file(file_name): Reads data from the given .json file and returns it as a Python dictionary.
	•	process_messages(file_choice, target_group): Sends messages to the target group based on the selected file. Randomized wait times are applied between each message.
	•	start_clients(): Starts the Telegram clients based on the provided account information.
	•	get_group_id(client, group_username): Fetches the group ID using the Telegram client and group username.
	•	main(): Manages the main flow of the program, including file selection, starting bots, and sending messages.

Troubleshooting
	•	Telegram API Errors: Ensure that the API keys are entered correctly.
	•	File Reading Errors: Ensure the files are formatted correctly and located at the correct file path.
	•	Group ID: Make sure the target group ID is correct. If the group has not been added to your bot, message sending will fail.
