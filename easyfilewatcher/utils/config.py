from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# os.path.join(os.path.normpath(os.path.dirname(__file__) + os.sep + os.pardir + os.sep + os.pardir)
DEFAULT_ENGINE = create_engine(
    'sqlite:///easyfilewatcher.sqlite')
DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=DEFAULT_ENGINE, expire_on_commit=False)
DB_NAME = "easyfilewatcherdb"
DIRECTORY_TABLE = "directories"


EASY_FILE_WATCHER_UNIT_ID = "id"
EASY_FILE_WATCHER_UNIT_SIZE = "size"
EASY_FILE_WATCHER_UNIT_FILE_PATH = "file_path"
EASY_FILE_WATCHER_UNIT_LAST_MODIFICATION = "last_modification"
