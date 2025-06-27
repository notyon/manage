import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO_URI = os.getenv("MONGO_URI")

OWNER_USERNAME = os.getenv("OWNER_USERNAME", "owner")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))
