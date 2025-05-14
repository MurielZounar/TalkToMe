import logging

from bot.bot import create_bot

logging.basicConfig(
    filename="talk_to_me.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    app = create_bot()
    app.run_polling()


if __name__ == "__main__":
    main()
