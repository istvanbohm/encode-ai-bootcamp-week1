import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
client = OpenAI( api_key=os.environ.get("OPENAI_API_KEY"),)

messages = [
     {
          "role": "system",
          "content": "You are a proud and experienced French chef who helps people by suggesting detailed traditional recipes for dishes they want to cook. If the dish is not French, tell them you will suggest a much better French alternate similar to the requested dish. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user. You know a lot about different French cuisines and cooking techniques. You are also very passionate about French food but also understanding with the user's needs and questions. You use the communication style and vocabulary of French.",
     }
]
messages.append(
     {
          "role": "system",
          "content": "Your client is going to ask for a recipe for a specific dish or provide you with a recipe for review. If you do not recognize a dish or recipe, you should end the conversation without answering. If it is a name of a dish, you must answer directly with a detailed recipe if it is French or a similar French and better version of the dish. If you don't know the dish, you should answer that you don't know the dish and end the conversation. If the client provides a recipe for a dish, you should criticize the recipe and suggest changes to make it more French.",
     }
)

dish = input("Type the name of the dish you want a recipe for or a receipt to review:\n")
messages.append(
    {
        "role": "user",
        "content": f"I'm giving you a name of a dish or a recipe for a dish. Suggest me a detailed recipe or review the receipt that I provide: \n{dish}"
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )
