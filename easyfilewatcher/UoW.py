
from sqlalchemy.orm import sessionmaker
from easyfilewatcher.utils.config import DEFAULT_SESSION_FACTORY
from easyfilewatcher.adapters.Repository import EasyFileWatcherUnitRepository


class EasyFileWatcherUoW:

    def __init__(self, session_factory: sessionmaker = DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.easy_file_watcher_repository = EasyFileWatcherUnitRepository(
            self.session)
        return self

    def __exit__(self, *args):
        self.session.expunge_all()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
