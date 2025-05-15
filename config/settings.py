import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")
BOT_KEY = os.getenv("BOT_KEY")
ROOT_PATH = Path(__file__).parent.parent
