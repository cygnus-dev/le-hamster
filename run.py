import main
from dotenv import load_dotenv
import os

load_dotenv()
main.ham.run(os.getenv("BOT_TOKEN"))