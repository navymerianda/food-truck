from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path('.') / 'env'
load_dotenv(dotenv_path=env_path)

class Config:
    '''Set Configuration variables from env file'''

    #Load in environment variables
    COLUMNS = os.getenv('COLUMNS')
    APP_TOKEN = os.getenv('APP_TOKEN')
    NUM_RESULTS = os.getenv('NUM_RESULTS')
    BASE_URL = os.getenv('BASE_URL')
    HEADERS = os.getenv('HEADERS')
