from dotenv import load_dotenv
load_dotenv()

from os import getenv
APP_SECRET_KEY = getenv("APP_SECRET_KEY")
