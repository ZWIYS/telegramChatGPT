from aiogram import types


def analytics(func: callable):
    total_messages = 0
    users = set()
    total_users = 0

    def analytics_wrapper(message: types.Message):
        nonlocal total_messages, total_users
        total_messages += 1

        if message.chat.id not in users:
            users.add(message.chat.id)
            total_users += 1

        with open("logs.txt", "w") as file:
            file.write(
                "total users: " + str(total_users)
                + "\ntotal messages: " + str(total_messages)
            )

        return func(message)

    return analytics_wrapper
