import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-VAzYa2yfTTttUMNvCBhluUKn"
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())