from pathlib import Path

from django.conf import settings


class Databases:
    def __init__(self, database_folder: str = 'databases'):
        self.database_dir: Path = settings.BASE_DIR / f'../{database_folder}'
        self.__create_db_dir()

    def __create_db_dir(self):
        self.database_dir.mkdir(parents=True, exist_ok=True)

    def get_databases(self):
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': self.database_dir / 'default.sqlite3',
            }
        }
