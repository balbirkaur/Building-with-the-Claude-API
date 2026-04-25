from common import client, add_user_message, add_assistant_message
from dotenv import load_dotenv
import os
load_dotenv()

def chat(messages):
    message = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL"),
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text
# --- Interactive chat loop ---
messages = []
while True:
    user_input = input("> ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat.")
        break
    add_user_message(messages, user_input)
    answer = chat(messages)
    print("Claude:", answer)
    add_assistant_message(messages, answer)  


# --- Two-turn scripted conversation ---
messages = []

add_user_message(messages, "Define quantum computing in one sentence")
answer = chat(messages)
print("Claude:", answer)
add_assistant_message(messages, answer)

add_user_message(messages, "Write another sentence")
final_answer = chat(messages)
print("Claude:", final_answer)
add_assistant_message(messages, final_answer)