from re import A
from pyrogram import Client, idle
from helpers.app_helpers import AppHelper


class Client(Client, AppHelper):
    def run(self):
        self.start()
        self.init_bot_info()
        self.send_awaking_msg()

        idle()

        self.stop()

    @staticmethod
    def error_handling(func):
        def wrapper(app, msg):
            try:
                func(app, msg)
            except Exception as e:
                app.send_error_msg(msg, e)

        return wrapper
