import os
from dotenv import load_dotenv

load_dotenv()

# API keys
API_KEY_STOCKS = os.environ.get("API_KEY_STOCKS")
API_KEY_NEWS = os.environ.get("API_KEY_NEWS")

# Email configuration
smtp_server = os.environ.get("SMTP_SERVER")
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")
smtp_port = os.environ.get("SMTP_PORT")



