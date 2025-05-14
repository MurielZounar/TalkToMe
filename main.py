import logging
import os

from dotenv import load_dotenv
from google import genai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

logging.basicConfig(
    filename="talk_to_me.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")
client = genai.Client(api_key=GEMINI_KEY)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Olá! 👋🏻
Eu sou o Zoun, seu robô tradutor! 🤖 
Antes de começarmos a traduzir tudo, aqui vão algumas informações importantes:
📌 Por enquanto, eu só traduzo textos do INGLÊS para o PORTUGUÊS.

📌 Você pode me mandar uma palavra, ou então uma frase completa, eu consigo traduzir sem problemas.

📌 /exemplo - É isso que você deve usar caso queira um exemplo de uso de uma palavra, basta enviar desse jeito: /exemplo sleep

💡 Para consultar todos os comandos disponíveis, é só me mandar um /help

⚒️ Ainda estou recebendo novas funcionalidades, assim que elas ficarem prontas, vou te avisar!""",
    )


def get_translation(english_text):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""Traduza isto para o português: {english_text}
Não responda nada além da resposta que solicitei, nada como "Claro!", "Com certeza", "Aqui está!", ect""",
    )
    print(response.text)
    return response.text


def get_example(word):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""Me dê um exemplo de uso da palavra "{word}" em inglês e depois me apresente a tradução da frase completa.
Use a seguinte estrutura:
Frase em inglês (frase em português)
Não responda mais nada além da resposta que solicitei, nada como "Claro!", "Com certeza", "Aqui está!", ect""",
    )
    print(response.text)
    return response.text


async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    english_text = update.message.text

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=get_translation(english_text)
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Estes são todos os comandos disponíveis:
/exemplo - Receber um exemplo de uso da palavra. Use assim: /exemplo sleep""",
    )


async def example(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Exemplo")
    if len(context.args) == 1:
        word = context.args[0]
        example_text = get_example(word)
    else:
        example_text = (
            "⚠️ Para te dar um exemplo, preciso que você me passe apenas uma palavra!"
        )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=example_text)


def create_bot():
    BOT_KEY = os.getenv("BOT_KEY")
    application = ApplicationBuilder().token(BOT_KEY).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    help_handler = CommandHandler("help", help)
    application.add_handler(help_handler)

    example_handler = CommandHandler("exemplo", example)
    application.add_handler(example_handler)

    translate_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), translate)
    application.add_handler(translate_handler)

    application.run_polling()


def main():
    create_bot()


if __name__ == "__main__":
    main()
