from pyrogram.types import Message

from client import Client as app
from helpers.punto import punto


@app.on_message(app.filters.command(["ru"]))
@app.error_handling
def ru_punto(_, msg: Message):
    punto(msg)


@app.on_message(app.filters.command(["en"]))
@app.error_handling
def en_punto(_, msg: Message):
    punto(msg)
