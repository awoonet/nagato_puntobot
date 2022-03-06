from os import getenv as env
from dotenv import load_dotenv
from client import Client

load_dotenv()

telegram_credentials = dict(
    session_name="session/nagato",
    api_id=env("API_ID"),
    api_hash=env("API_HASH"),
    bot_token=env("BOT_TOKEN"),
    plugins={"root": "plugins"},
)

app = Client(**telegram_credentials)

app.config_messages = env("CONFIG_MESSAGES")

app.run()
