from config.settings import GEMINI_KEY
from google import genai

client = genai.Client(api_key=GEMINI_KEY)


def translate(english_text: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""Traduza isto para o português: {english_text}
Não responda nada além da resposta que solicitei, nada como "Claro!", "Com certeza", "Aqui está!", ect""",
    )
    return response.text


def get_example(word: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""Me dê um exemplo de uso da palavra "{word}" em inglês e depois me apresente a tradução da frase completa.
Use a seguinte estrutura:
Frase em inglês (frase em português)
Não responda mais nada além da resposta que solicitei, nada como "Claro!", "Com certeza", "Aqui está!", ect""",
    )
    return response.text
