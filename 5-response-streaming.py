from common import client, add_user_message
from dotenv import load_dotenv
import os
load_dotenv()

messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

stream = client.messages.create(
    model=os.getenv("ANTHROPIC_MODEL"),
    max_tokens=1000,
    messages=messages,
    stream=True
)

for event in stream:
    print(event)
    
#     Simplified Text Streaming

# Rather than manually parsing events, you can use the SDK's simplified streaming interface that extracts just the text content:

with client.messages.stream(
    model=os.getenv("ANTHROPIC_MODEL"),
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")
        
#         Getting the Complete Message

# While streaming individual chunks is great for user experience, you often need the complete message for storage or further processing. After streaming completes, you can get the assembled final message:

with client.messages.stream(
    model=os.getenv("ANTHROPIC_MODEL"),
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        # Send each chunk to your client
        pass
    
    # Get the complete message for database storage
    final_message = stream.get_final_message()