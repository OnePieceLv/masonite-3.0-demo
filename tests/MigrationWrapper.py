import subprocess

from masonite.helpers import config, HasColoredCommands
from masonite.packages import add_venv_site_packages
from masoniteorm.migrations import Migration


class MigrationWrapper(HasColoredCommands):
    def __init__(self, connection=None):
        self._ran = []
        self._notes = []
        from config import database

        if not connection or connection == "default":
            connection = database.DATABASES["default"]
        self.migrator = Migration(connection)
        self.migrator.create_table_if_not_exists()

    def run(self):
        self.migrator.migrate()

        return self

    def rollback(self):
        self.migrator.rollback()

        return self

    def refresh(self):
        self.run()
        self.rollback()

    def reset(self):
        self.migrator.reset()

        return self

    def ran(self):
        return self._ran


def has_unmigrated_migrations():
    return False
