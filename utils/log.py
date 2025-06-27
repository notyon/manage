
from config import LOG_GROUP_ID
from pyrogram.types import Message

async def send_log(client, text: str):
    if LOG_GROUP_ID:
        try:
            await client.send_message(LOG_GROUP_ID, text)
        except:
            pass
