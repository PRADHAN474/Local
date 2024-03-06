# Telegram Bot with Random Buttons for Class Notes

This Telegram bot provides users with access to class notes based on the button clicked. Users must join a specific channel to access the notes.

## Features

- Displays class notes based on button clicks
- Requires users to join a specific channel to access notes
- Allows the owner to import files directly to the database using special commands

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   
Here's an example of a `README.md` file for your Telegram bot project, including instructions for deployment on Heroku and an embedded Heroku Deploy button:

```markdown
# Telegram Bot with Random Buttons for Class Notes

This Telegram bot provides users with access to class notes based on the button clicked. Users must join a specific channel to access the notes.

## Features

- Displays class notes based on button clicks
- Requires users to join a specific channel to access notes
- Allows the owner to import files directly to the database using special commands

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file with the following variables:
     ```
     BOT_TOKEN=your_bot_token
     MONGODB_URI=your_mongodb_uri
     ```
   - Replace `your_bot_token` with your Telegram bot token and `your_mongodb_uri` with your MongoDB URI.

4. Run the bot:
   ```bash
   python bot.py
   ```

## Deploy to Heroku

You can deploy this bot to Heroku with the following steps:

1. Click the button below to deploy the bot to Heroku:

[![ʜᴇʀᴏᴋᴜ](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PRADHAN474/Local)


2. Set the following environment variables in your Heroku app settings:
   - `BOT_TOKEN`: Your Telegram bot token
   - `MONGODB_URI`: Your MongoDB URI

3. Scale up the dynos to at least one to start your bot.

## Support

For support or questions, please join our Telegram support group: [@BWANDARLOK](https://t.me/BWANDARLOK).
