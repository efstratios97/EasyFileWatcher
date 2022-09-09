from typing import List

from sqlalchemy.orm import Session

from easyfilewatcher.domain.EasyFileWatcherUnit import EasyFileWatcherUnit


class EasyFileWatcherUnitRepository:

    def __init__(self, session: Session):
        self.session = session

    def add_all(self, easy_file_watcher_units: List[EasyFileWatcherUnit]) -> bool:
        try:
            self.session.add_all(easy_file_watcher_units)
            return True
        except Exception as e:
            print(e)
            return False

    def add(self, easy_file_watcher_unit: EasyFileWatcherUnit) -> bool:
        try:
            self.session.add(easy_file_watcher_unit)
            return True
        except Exception as e:
            print(e)
            return False

    def get_all_by_id(self, directory_watcher_id: str) -> EasyFileWatcherUnit:
        return self.session.query(EasyFileWatcherUnit).filter_by(directory_watcher_id=directory_watcher_id).all()

    def all(self) -> List[EasyFileWatcherUnit]:
        return self.session.query(EasyFileWatcherUnit).all()

    def delete(self, easy_file_watcher_unit: EasyFileWatcherUnit) -> bool:
        try:
            self.session.delete(easy_file_watcher_unit)
            return True
        except Exception as e:
            print(e)
            return False
