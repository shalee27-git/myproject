import django
import os
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()
from core.models import TelegramUser

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    if username:
        TelegramUser.objects.get_or_create(username=username)
    await update.message.reply_text(f"Hello {username}!")

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()