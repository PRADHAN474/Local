# config.py

import os
import json

def load_config():
    # Check if running on Heroku
    if 'DATABASE_URL' in os.environ:
        # Running on Heroku, load config from environment variables
        return {
            'BOT_TOKEN': os.environ.get('BOT_TOKEN'),
            'DATABASE_URL': os.environ.get('DATABASE_URL')
        }
    else:
        # Not running on Heroku, load config from app.json
        with open('app.json', 'r') as file:
            config_data = json.load(file)
        return {
            'BOT_TOKEN': config_data['env']['BOT_TOKEN'],
            'DATABASE_URL': config_data['env']['DATABASE_URL']
        }

config = load_config()
