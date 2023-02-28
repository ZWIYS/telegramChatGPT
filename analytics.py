from aiogram import types
import logs


def analytics(func: callable):
    total_messages = logs.total_messages
    users = set()
    total_users = 0

    def analytics_wrapper(message: types.Message):
        nonlocal total_messages, total_users
        total_messages += 1

        if message.chat.id not in users:
            users.add(message.chat.id)
            total_users += 1

        with open("logs.py", "w") as file:
            file.write(
                "total_users = " + str(total_users)
                + "\ntotal_messages = " + str(total_messages)
            )

        return func(message)

    return analytics_wrapper
