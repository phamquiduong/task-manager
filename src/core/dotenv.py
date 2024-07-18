from pathlib import Path
from time import sleep

from django.conf import settings
from dotenv import load_dotenv


class DotEnv:
    def __init__(self, dotenv_folder: str = ''):
        self.dotenv_dir: Path = settings.BASE_DIR / f'..{dotenv_folder}'
        self.__create_db_dir()

    def __create_db_dir(self):
        self.dotenv_dir.mkdir(parents=True, exist_ok=True)

    def load(self, dotenv_file_name: str = '.env'):
        while not load_dotenv(self.dotenv_dir / dotenv_file_name):
            print('Load environment file failed. Will try after 5 seconds..')
            sleep(5)
