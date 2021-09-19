from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_CREDENTIALS = getenv('DB_CREDENTIALS')