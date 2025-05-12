from os import getenv
from dotenv import load_dotenv
import os

load_dotenv()
# Load environment variables from .env file

PLISIO_API = getenv('PLISIO_API')
BOT_TOKEN = getenv('BOT_TOKEN')