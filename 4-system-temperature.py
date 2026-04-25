from common import client, add_user_message
from dotenv import load_dotenv
import os
load_dotenv()

def chat(messages,system=None,temperature=1.0):
    parameters = {
        "model": os.getenv("ANTHROPIC_MODEL"),
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    if system:
        parameters["system"] = system
    message = client.messages.create(
        **parameters
    )
    return message.content[0].text
# --- Interactive chat loop ---
messages = []

add_user_message(messages, "90's kids usual habits that 2000's kids won't understand?")
answer = chat(messages,temperature=1.0)
print("Claude:", answer)

