import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

APP_ID = os.environ.get("APPID")
API_KEY = os.environ.get("APIKEY")
AUTHORIZATION = os.environ.get("AUTHORIZATION")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")
