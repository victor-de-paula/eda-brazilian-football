from dotenv import load_dotenv
import os

load_dotenv() # Used to load environment variables from .env file

rapid_api_host = os.getenv('RAPIDAPI_HOST')
rapid_api_key = os.getenv('RAPIDAPI_KEY')