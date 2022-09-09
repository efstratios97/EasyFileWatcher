from sqlalchemy import Table, Column, String, Integer, Float
from sqlalchemy.orm import registry

from utils.config import (DIRECTORY_TABLE, EASY_FILE_WATCHER_UNIT_ID, EASY_FILE_WATCHER_UNIT_FILE_PATH,
                          EASY_FILE_WATCHER_UNIT_LAST_MODIFICATION, EASY_FILE_WATCHER_UNIT_SIZE, DEFAULT_ENGINE)
from domain.EasyFileWatcherUnit import EasyFileWatcherUnit, class_attributes_easy_file_watcher_unit

mapper_registry = registry()

easy_file_watcher_units = Table(DIRECTORY_TABLE, mapper_registry.metadata,
                                Column("ID", Integer, primary_key=True),
                                Column(class_attributes_easy_file_watcher_unit.get(
                                    EASY_FILE_WATCHER_UNIT_ID), String(255), nullable=False),
                                Column(class_attributes_easy_file_watcher_unit.get(EASY_FILE_WATCHER_UNIT_FILE_PATH),
                                       String(513), nullable=False),
                                Column(class_attributes_easy_file_watcher_unit.get(EASY_FILE_WATCHER_UNIT_LAST_MODIFICATION),
                                       Float, nullable=False),
                                Column(class_attributes_easy_file_watcher_unit.get(EASY_FILE_WATCHER_UNIT_SIZE),
                                       Integer, nullable=False),
                                )


def init_tables():
    mapper_registry.map_imperatively(
        EasyFileWatcherUnit, easy_file_watcher_units)
    mapper_registry.metadata.create_all(DEFAULT_ENGINE)
