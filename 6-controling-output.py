from common import client, add_user_message, add_assistant_message, chat
from dotenv import load_dotenv
import json
load_dotenv()

# This technique works by:

#     The user message tells Claude what to generate
#     The prefilled assistant message makes Claude think it already started a markdown code block
#     Claude continues by writing just the JSON content
#     When Claude tries to close the code block with ```, the stop sequence immediately ends generation


messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])
    
# Clean up and parse the JSON
clean_json = json.loads(text.strip())