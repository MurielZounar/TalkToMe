from bot.translator import get_example, translate
from telegram import Update
from telegram.ext import ContextTypes


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


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Estes são todos os comandos disponíveis:
/exemplo - Receber um exemplo de uso da palavra. Use assim: /exemplo sleep""",
    )


async def example(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 1:
        word = context.args[0]
        example_text = get_example(word)
    else:
        example_text = (
            "⚠️ Para te dar um exemplo, preciso que você me passe apenas uma palavra!"
        )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=example_text)


async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    english_text = update.message.text
    translated_text = translate(english_text)

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=translated_text
    )
