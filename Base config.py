"""
CONF 1

response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )


CONF 2

response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.3,
        max_tokens=1500,
        top_p=0.3,
        frequency_penalty=0.0,
        presence_penalty=0.3,
        stop=[" Human:", " AI:"]
    )
"""