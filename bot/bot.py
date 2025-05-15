from bot.commands import example, help, speak, start, translate
from config.settings import BOT_KEY
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


def create_bot():
    app = ApplicationBuilder().token(BOT_KEY).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("exemplo", example))
    app.add_handler(CommandHandler("falar", speak))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), translate))

    return app
