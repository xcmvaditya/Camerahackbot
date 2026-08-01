# 📸 CameraHackBot — Telegram Camera Hack Tool

> **Developed by:** GENIUS HACKER ADITYA  
> **Purpose:** Educational & Ethical Hacking Demonstration

---

## 🔥 Features
- ✅ Welcome Screen with Join Buttons
- ✅ YouTube & WhatsApp Group Integration
- ✅ Generate Unlimited Victim Links
- ✅ Auto-Save Victim Data (`links.txt`)
- ✅ 24/7 Hosting Support (PM2)
- ✅ No Real Join Required — Skip Option Available

---

## 📦 Requirements
- Termux (Android) or any Linux Terminal
- Python 3.7+
- Internet Connection

---

## 🚀 Quick Installation (Termux)

```bash
# 1. Update & Upgrade
pkg update && pkg upgrade -y

# 2. Install Python & Pip
pkg install python -y
pip install --upgrade pip

# 3. Clone Repository
git clone https://github.com/xcmvaditya/Camerahackbot.git
cd Camerahackbot

# 4. Install Dependencies
pip install python-telegram-bot

# 5. Run Bot (No Token Change Needed!)
python camerahackbot.py
```

✅ **That's it!** Bot will start immediately.  
🔹 **No token change needed** — already configured.

---

## 🤖 Bot Commands (After Running)

| Command | Action |
|---------|--------|
| `/start` | Get your victim link |
| `/stats` | Check total victims |
| `/help` | Show help menu |

---

## 🔥 24/7 Hosting with PM2

```bash
# Install PM2
npm install -g pm2

# Start Bot in Background
pm2 start camerahackbot.py --name camera-bot --interpreter python

# Check Status
pm2 status

# View Logs
pm2 logs camera-bot

# Restart Bot
pm2 restart camera-bot

# Stop Bot
pm2 stop camera-bot

# Auto-Start on Boot
pm2 save
pm2 startup
```

---

## 📁 File Structure

```
Camerahackbot/
├── camerahackbot.py   # Main bot code (token pre-configured)
├── links.txt          # Auto-generated victim data
├── requirements.txt   # Dependencies
└── README.md          # This file
```

---

## 🔧 Troubleshooting

### Error: `No module named 'telegram'`
```bash
pip install python-telegram-bot
```

### Error: `pip: command not found`
```bash
pkg install python-pip -y
```

### Error: `git: command not found`
```bash
pkg install git -y
```

---

## ⚠️ Disclaimer
> This tool is for **educational & ethical security research only**.  
> Misuse is strictly prohibited. Use at your own risk.

---

## 📱 Connect with Developer

- 📺 **YouTube:** [@geniushacker29](https://youtube.com/@geniushacker29)
- 💬 **WhatsApp Group:** [Join Here](https://chat.whatsapp.com/GcDcK5iL4hr2rD0IyI1SDW)

---

**Enjoy! 🚀**
