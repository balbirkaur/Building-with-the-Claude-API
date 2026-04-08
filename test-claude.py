from dotenv import load_dotenv
import os
from anthropic import Anthropic


load_dotenv(override=True)

client = Anthropic(
    base_url=os.getenv("ANTHROPIC_BASE_URL"),
    api_key=os.getenv("ANTHROPIC_AUTH_TOKEN"),
)

response = client.messages.create(
    model = "openai/gpt-4o-mini",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Explain Claude simply."}
    ]
)

print(response.content[0].text)