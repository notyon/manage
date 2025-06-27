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
