import os
from dotenv import load_dotenv

# Muat isi file .env
load_dotenv()

# API Telegram
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# MongoDB
MONGO_URI = os.getenv("MONGO_URI")

# Identitas bot & admin
OWNER_USERNAME = os.getenv("OWNER_USERNAME")     # tanpa '@'
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP")       # tanpa '@'
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID"))    # grup log (pakai -100...)

# Validasi wajib
REQUIRED_VARS = ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URI", "OWNER_USERNAME", "SUPPORT_GROUP", "LOG_GROUP_ID"]
missing = [var for var in REQUIRED_VARS if not os.getenv(var)]
if missing:
    raise Exception(f"❌ Variabel berikut belum disetel di .env: {', '.join(missing)}")
