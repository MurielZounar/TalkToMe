import os
from pathlib import Path

from config.settings import ROOT_PATH


def create_file(id, first_name, last_name):
    try:
        file_path = Path(ROOT_PATH / "history")
        if not file_path.exists():
            os.mkdir(ROOT_PATH / "history")

        with open(get_path(id, first_name, last_name), "a") as file:
            pass
    except IOError as err:
        print(
            f"Houve um erro ao gerar o arquivo de histórico\nDescrição do erro: {err}"
        )


def write_message(id, first_name, last_name, user_message, bot_message):
    try:
        with open(
            get_path(id, first_name, last_name), "a", encoding="utf-8", newline=""
        ) as file:
            if user_message:
                file.write(f"{first_name}: {user_message}\n")

            if bot_message:
                file.write(f"Zoun: {bot_message}")
    except IOError as err:
        print(
            f"Houve um erro ao registrar a mensagem no arquivo\nDescrição do erro: {err}"
        )


def get_path(id, first_name, last_name):
    return ROOT_PATH / "history" / f"{id}_{first_name}_{last_name}.txt"


def file_exists(id, first_name, last_name):
    file_path = Path(get_path(id, first_name, last_name))
    if file_path.exists():
        return True

    return False
