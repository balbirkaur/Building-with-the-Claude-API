from common import client, add_user_message, add_assistant_message
from dotenv import load_dotenv
import os
load_dotenv()

from common import client, add_user_message, add_assistant_message
def chat(messages):
    system="""
        You are patient and helpful maths tutor.
        Do not directly answer the question. Instead, guide the student through the problem-solving process by asking questions and providing hints.
        Guide them to solution step by step."""
    message = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL"),
        max_tokens=1000,
        messages=messages,
        system=system
    )
    return message.content[0].text
# --- Interactive chat loop ---
messages = []

add_user_message(messages, "There are 3 apples and 4 oranges in a basket. How many pieces of fruit are there in total?")
answer = chat(messages)
print("Claude:", answer)

