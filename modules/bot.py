import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    filename="talk_to_me.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Bot:
    def __init__(self):
        load_dotenv()
        BOT_KEY = os.getenv("BOT_KEY")
        self.application = ApplicationBuilder().token(BOT_KEY).build()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🤖 Olá, sou seu robô tradutor, fale comigo!",
        )

    def create_handlers(self):
        start_handler = CommandHandler("start", self.start)
        self.application.add_handler(start_handler)

    def run_polling(self):
        self.application.run_polling()
