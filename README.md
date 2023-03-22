ReminderBotTelegram

This is a Telegram bot that allows you to set reminders for yourself or for groups.

Installation

    Clone the repository:

bash

git clone https://github.com/sahilkarnany/ReminderBotTelegram.git

    Install the dependencies:

bash

pip install -r requirements.txt

    Create a Telegram bot and get the API token. You can follow the official Telegram documentation to create a new bot.

    Copy the API token to the config.ini file.

ini

[telegram]
token = YOUR_TELEGRAM_BOT_TOKEN_HERE

Usage

    Run the main.py script to start the bot.

bash

python main.py

    Open Telegram and search for your bot.

    Send the /start command to the bot to start using it.

Commands

    /start: Start the bot and get a list of available commands.
    /help: Get help on how to use the bot.
    /remind: Set a reminder for yourself or for a group. You can specify the time and the message for the reminder.
    /list: List all your current reminders.
    /delete: Delete a specific reminder by its ID.
    /deleteall: Delete all your current reminders.

Contributing

Contributions are welcome! Please read the CONTRIBUTING.md file for more information on how to contribute.
License

This project is licensed under the MIT License. See the LICENSE.md file for details.
