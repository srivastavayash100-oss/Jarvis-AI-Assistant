from openai import OpenAI

client = OpenAI(
    api_key= "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",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named jarvis, skilled in general tasks like Alexa and Google."
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming."
        }
    ]
)
print(completion.choices[0].message.content)

