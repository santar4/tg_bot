import os
from dotenv import load_dotenv


load_dotenv()



bot_token = os.getenv('Token')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, 'data', 'data_quotes.json')

