import logging
import os
from pathlib import Path

from django.conf import settings


class Logging:
    def __init__(self, log_folder: str = 'logs'):
        self.log_dir: Path = settings.BASE_DIR / f'../{log_folder}'
        self.__create_db_dir()

    def __create_db_dir(self):
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def get_config(self):
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'format': '[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S'
                },
            },
            'handlers': {
                'console': {
                    'level': os.getenv('LOG_LEVEL', 'DEBUG'),
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                },
                'file': {
                    'level': os.getenv('LOG_LEVEL'),
                    'class': 'logging.handlers.RotatingFileHandler',
                    'formatter': 'default',
                    'filename': self.log_dir / 'file.log',
                    'maxBytes': 50000,
                    'backupCount': 5,
                },

            },
            'loggers': {
                'default': {
                    'handlers': os.getenv('LOG_HANDLER', 'console').split(','),
                    'level': os.getenv('LOG_LEVEL'),
                    'propagate': True,
                }
            },
        }

    @staticmethod
    def get_logger():
        return logging.getLogger('default')


logger = Logging.get_logger()
