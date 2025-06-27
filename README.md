# Telegram Manage Bot

Bot Telegram untuk mengelola grup dengan fitur lengkap:

## 🛠 Fitur Utama

- Welcome message yang bisa diatur
- Auto reply /filter <pesan>
- Force subscribe (mute + tombol unmute)
- Perintah admin: /mute /ban /kick /unban /unmute
- Zodiak checker: /zodiak 21-03
- Cek anomali lucu: /cekanomali
- Konfigurasi via DM bot (/setforce /setwelcome)
- Logging user ke grup log

## 🧾 Instalasi

```bash
pip install -r requirements.txt
```

## ⚙️ Setup .env

Buat file `.env` dan isi seperti ini:

```
API_ID=123456
API_HASH=abc123hash
BOT_TOKEN=token:bot
MONGO_URI=mongodb://localhost:27017
OWNER_USERNAME=namakamu
SUPPORT_GROUP=namagroup
LOG_GROUP_ID=-100xxxxxxxxxx
```

## 🚀 Jalankan

```bash
python bot.py
```
