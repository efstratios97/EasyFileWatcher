from dataclasses import dataclass

from easyfilewatcher.utils.config import (EASY_FILE_WATCHER_UNIT_ID, EASY_FILE_WATCHER_UNIT_FILE_PATH,
                                          EASY_FILE_WATCHER_UNIT_LAST_MODIFICATION, EASY_FILE_WATCHER_UNIT_SIZE)

class_attributes_easy_file_watcher_unit = {
    EASY_FILE_WATCHER_UNIT_ID: "directory_watcher_id",
    EASY_FILE_WATCHER_UNIT_FILE_PATH: "filepath",
    EASY_FILE_WATCHER_UNIT_LAST_MODIFICATION: "last_modification",
    EASY_FILE_WATCHER_UNIT_SIZE: "size",
}


@dataclass
class EasyFileWatcherUnit:
    directory_watcher_id: str
    filepath: str
    last_modification: str
    size: int

    def __le__(self,  __o: object):
        return ((self.size) <= (__o.size))

    def __lt__(self, __o: object):
        return ((self.size) < (__o.size))

    def __gt__(self, __o: object):
        return ((self.size) > (__o.size))

    def __le__(self, __o: object):
        return ((self.size) <= (__o.size))

    def __ge__(self, __o: object):
        return ((self.size) >= (__o.size))

    def __eq__(self, __o: object) -> bool:
        try:
            if not isinstance(__o, EasyFileWatcherUnit):
                return False
            return True if hash((self.filepath, self.last_modification, self.size)) == hash((__o.filepath, __o.last_modification, __o.size)) else False
        except Exception as e:
            print(e)

    def __hash__(self) -> int:
        return hash((self.filepath, self.last_modification, self.size))
