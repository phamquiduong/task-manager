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
            },
            'authentication': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': self.database_dir / 'authentication.sqlite3',
            },
            'session': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': self.database_dir / 'session.sqlite3',
            }
        }

    def get_routers(self):
        return [
            'core.databases.AuthenticationRouter',
            'core.databases.SessionRouter',
            'core.databases.DefaultRouter',
        ]


class AuthenticationRouter:
    route_app_labels = ['authentication']
    db_name = 'authentication'

    def db_for_read(self, model, **_):
        if model._meta.app_label in self.route_app_labels:    # pylint: disable=W0212
            return self.db_name
        return None

    def db_for_write(self, model, **_):
        if model._meta.app_label in self.route_app_labels:    # pylint: disable=W0212
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **_):
        if (
            obj1._meta.app_label in self.route_app_labels     # pylint: disable=W0212
            or obj2._meta.app_label in self.route_app_labels  # pylint: disable=W0212
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, _=None, **__):
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


class SessionRouter:
    route_app_labels = ['session']
    db_name = 'session'

    def db_for_read(self, model, **_):
        if model._meta.app_label in self.route_app_labels:    # pylint: disable=W0212
            return self.db_name
        return None

    def db_for_write(self, model, **_):
        if model._meta.app_label in self.route_app_labels:    # pylint: disable=W0212
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **_):
        if (
            obj1._meta.app_label in self.route_app_labels     # pylint: disable=W0212
            or obj2._meta.app_label in self.route_app_labels  # pylint: disable=W0212
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, _=None, **__):
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


class DefaultRouter:
    other_route_app_labels = [
        AuthenticationRouter.route_app_labels,
        SessionRouter.route_app_labels
    ]
    db_name = 'default'

    def db_for_read(self, model, **_):
        if model._meta.app_label not in self.other_route_app_labels:    # pylint: disable=W0212
            return self.db_name
        return None

    def db_for_write(self, model, **_):
        if model._meta.app_label not in self.other_route_app_labels:    # pylint: disable=W0212
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **_):
        if (
            obj1._meta.app_label not in self.other_route_app_labels     # pylint: disable=W0212
            or obj2._meta.app_label not in self.other_route_app_labels  # pylint: disable=W0212
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, _=None, **__):
        if app_label not in self.other_route_app_labels:
            return db == self.db_name
        return None
