from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv(override=True)
for var in ("ANTHROPIC_BASE_URL", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_MODEL"):
    if not os.getenv(var):
        raise EnvironmentError(f"Missing required environment variable: {var}")
client = Anthropic(
    base_url=os.getenv("ANTHROPIC_BASE_URL"),
    api_key=os.getenv("ANTHROPIC_AUTH_TOKEN"),
)

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

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