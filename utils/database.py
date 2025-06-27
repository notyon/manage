from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['manage_bot']

# Koleksi mute tracking
mute_col = db['mutes']

def mute_user(chat_id: int, user_id: int):
    """Simpan user sebagai muted"""
    mute_col.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"muted": True}},
        upsert=True
    )

def unmute_user(chat_id: int, user_id: int):
    """Hapus status mute"""
    mute_col.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"muted": False}},
        upsert=True
    )

def is_user_muted(chat_id: int, user_id: int) -> bool:
    """Cek apakah user masih muted"""
    data = mute_col.find_one({"chat_id": chat_id, "user_id": user_id})
    return bool(data and data.get("muted", False))

# Koleksi welcome
welcome_col = db['welcome']

def set_welcome(chat_id: int, text: str):
    welcome_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"text": text}},
        upsert=True
    )

def get_welcome(chat_id: int) -> str:
    data = welcome_col.find_one({"chat_id": chat_id})
    return data["text"] if data else None
