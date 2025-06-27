from config import LOG_GROUP_ID

async def send_log(text: str, client=None):
    if LOG_GROUP_ID and client:
        try:
            await client.send_message(LOG_GROUP_ID, text)
        except Exception as e:
            print(f"[LOG ERROR] Gagal kirim log: {e}")
