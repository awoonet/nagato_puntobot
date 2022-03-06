from pyrogram import filters, Client as app
from pyrogram.types import Message, User
from plugins.chars_en import en
from plugins.chars_ru import ru

chars = dict(ru=ru, en=en)


def fetch_name(user: User) -> str:
    """Возвращает username, имя с фамилией или просто имя
    отформатированное в соответствии с полученной командой."""
    if user.username is not None:
        return f"@{user.username}"
    elif user.last_name is not None:
        return f"{user.first_name} {user.last_name}"
    else:
        return user.first_name


def fetch_text(msg: Message) -> str:
    """Возвращает caption, text или ничего из сообщения"""
    if msg.text is not None:
        return msg.text.markdown
    elif msg.caption is not None:
        return msg.caption.markdown
    else:
        return ""


def punto(msg: Message) -> None:
    command = msg.command[0]
    char = chars[command.replace("@yukinagato_puntobot", "")]

    if msg.reply_to_message:
        msg = msg.reply_to_message

    user = fetch_name(msg.from_user)
    text = fetch_text(msg).replace(f"/{command}", "")

    ptxt = "".join(list(map(lambda i: char.get(i, i), text)))

    stxt = f"{user} ошибся в раскладке и написал:\n{ptxt}"

    msg.reply(stxt, reply_to_message_id=msg.message_id, disable_notification=True)


@app.on_message(filters.command(["ru"]))
def ru_punto(_, msg: Message):
    punto(msg)


@app.on_message(filters.command(["en"]))
def en_punto(_, msg: Message):
    punto(msg)
