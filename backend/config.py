import os

from dotenv import load_dotenv

load_dotenv()

IP = os.getenv("SERVER")
PORT = os.getenv("PORT_BACK")