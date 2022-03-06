from pyrogram import filters, Client as app
from pyrogram.types import Message

from helpers.punto import punto


@app.on_message(filters.command(["ru"]))
@app.error_handling
def ru_punto(_, msg: Message):
    punto(msg)


@app.on_message(filters.command(["en"]))
@app.error_handling
def en_punto(_, msg: Message):
    punto(msg)
