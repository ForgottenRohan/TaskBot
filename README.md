## Telegram Bot Setup Guide

### Prerequisites

- Python installed on your system (preferably Python 3.7+)
- A Telegram account
- Basic knowledge of Python and command-line interface

### Steps

1. **Create a Bot on Telegram**
    
    - Open the Telegram app and search for `@BotFather`.
    - Start a chat with `@BotFather` and send the command `/newbot`.
    - Follow the instructions to create a new bot. You will receive a token after creating the bot. Save this token securely.
2. **Set Up Your Development Environment**
    
    - Install `python-telegram-bot` library using pip:
```bash 
pip install python-telegram-bot --upgrade
```
3. **Write Telegram bot token to conf.py**
```python
TOKEN='YOUR_TOKEN'
```
4. **Run Your Bot**

	- Open a command-line interface and navigate to the directory where your `bot.py` is located.
	- Run the bot using the following command:
```bash 
python bot.py
```
5. Your bot should now be running. You can interact with it via Telegram by searching for your bot's username and sending commands like `/start`, `/add <task>`, `/list`, and `/done <task number>'.
