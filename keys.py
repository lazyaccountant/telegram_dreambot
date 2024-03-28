import os
from dotenv import load_dotenv

load_dotenv()

bot_key = os.getenv("TELEGRAM_API_KEY")
hf_key = os.getenv("HUGGINGFACE_API_KEY")

if __name__ == "__main__":
	print(bot_key)


