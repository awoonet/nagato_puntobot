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

Client(**telegram_credentials).run()
