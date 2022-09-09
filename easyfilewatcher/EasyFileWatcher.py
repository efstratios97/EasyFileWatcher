import os
import uuid

from types import FunctionType
from typing import List, Optional

from sqlalchemy_utils.functions import create_database, database_exists

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor

from easyfilewatcher.utils.config import DEFAULT_ENGINE

from easyfilewatcher.adapters.ORM import init_tables

from easyfilewatcher.domain.EasyFileWatcherUnit import EasyFileWatcherUnit

from easyfilewatcher.UoW import EasyFileWatcherUoW


class EasyFileWatcher:

    def __init__(self) -> None:
        self.__int_workflow_scheduler()
        self.__init_database()
        self.__init_database_tables()

    def __int_workflow_scheduler(self) -> None:
        """This method initializes and configures the Scheduler for the EasyFileWatcher.
            :returns: None
            :rtype: None
        """
        global workflow_scheduler
        jobstores = {
            'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
        }
        executors = {
            'default': {'type': 'threadpool', 'max_workers': 20},
            'processpool': ProcessPoolExecutor(max_workers=20)
        }
        job_defaults = {
            'coalesce': False,
            'max_instances': 10000
        }
        workflow_scheduler = BackgroundScheduler()
        workflow_scheduler.configure(jobstores=jobstores,
                                     executors=executors, job_defaults=job_defaults)
        workflow_scheduler.start()

    def __init_database(self) -> None:
        """This method initializes the database for the EasyFileWatcher if it doesn't exist yet.
            :returns: None
            :rtype: None
        """
        try:
            if not database_exists(DEFAULT_ENGINE.url):
                create_database(DEFAULT_ENGINE.url)
        except Exception as e:
            print(e)
            print("database exists")

    def __init_database_tables(self) -> None:
        """This method initializes the database tables for the EasyFileWatcher if they don't exist yet.
            :returns: None
            :rtype: None
        """
        try:
            init_tables()
        except Exception as e:
            print(e)
            print("database tables already exist")

    def delete_easy_file_watcher(self, directory_watcher_id) -> bool:
        """This method deletes an EasyFileWatcher. It returns True at success and False at failure.
            :returns: None
            :rtype: None
        """
        try:
            workflow_scheduler.remove_job(
                job_id=directory_watcher_id)
        except Exception as e:
            workflow_scheduler.print_jobs()
            print(e)
        try:
            with EasyFileWatcherUoW() as uow:
                file_watcher_units_in_db = uow.easy_file_watcher_repository.get_all_by_id(
                    directory_watcher_id=directory_watcher_id)
                [uow.easy_file_watcher_repository.delete(
                    easy_file_watcher) for easy_file_watcher in file_watcher_units_in_db]
                uow.commit()
        except Exception as e:
            workflow_scheduler.print_jobs()
            print(e)
            return False
        return True

    def get_directory_watcher_jobs(self) -> list:
        """This method return a list of current EasyFileWatcher Jobs. 
        Good way to retrieve DirectoryWatcherID if not initially provided.
            :returns: list of EasyFileWatcher Jobs
            :rtype: list
        """
        return workflow_scheduler.get_jobs()

    @staticmethod
    def __get_all_easy_file_watcher_units(directory_path: str, directory_watcher_id: str) -> List[EasyFileWatcherUnit]:
        """This method returns all content and its metadata from a specified directory path. Temporary contents/files are disregarded.
            :param str directory_path: path of directory to watch
            :param str directory_watcher_id: assigned ID of watcher
            :returns: List of EasyFileWatcherUnits
            :rtype: List[EasyFileWatcherUnit]
        """
        file_contents = []
        for (dirpath, dirnames, filenames) in os.walk(directory_path):
            [file_contents.append(EasyFileWatcherUnit(**{
                "directory_watcher_id": directory_watcher_id,
                "filepath": os.path.join(dirpath, file),
                "size": os.path.getsize(os.path.join(dirpath, file)),
                "last_modification": os.path.getmtime(os.path.join(dirpath, file))})) for file in filenames if not "~$" in file]
        return file_contents

    @staticmethod
    def __get_all_current_filewatcher_units_by_directory_watcher_id(directory_watcher_id) -> List[EasyFileWatcherUnit]:
        """This method returns all content and its metadata from database associated to a certain EasyFileWatcher.
            :param str directory_watcher_id: assigned ID of watcher
            :returns: List of EasyFileWatcherUnits
            :rtype: List[EasyFileWatcherUnit]
        """
        with EasyFileWatcherUoW() as uow:
            current_file_watcher_units = uow.easy_file_watcher_repository.get_all_by_id(
                directory_watcher_id=directory_watcher_id)
            uow.commit()
        return current_file_watcher_units

    def add_directory_to_watch(self, directory_path: str, callback: FunctionType,
                               callback_param: Optional[dict] = None, directory_watcher_id: Optional[str] = None,
                               event_on_deletion: Optional[bool] = False) -> None:
        """This method registers the directory of interest to watch. 
        It further requires the function signature. 
        Parameters to the function can be passed as a dictionary. 
        Passing a directory_watcher_id is highly recommended as it can be used to delete a certain FileWatcher. 
            :param str directory_path: path of directory to watch
            :param func callback: custom user to function to be executed at change in directory
            :param Optional[dict] callback_param: parameters to be passed to callback function
            :param Optional[str] directory_watcher_id: assigned ID of watcher
            :param Optional[bool] event_on_deletion: shall an event be triggered at deletion of File
            :returns: List of EasyFileWatcherUnits
            :rtype: List[EasyFileWatcherUnit]
        """
        if directory_watcher_id is None:
            directory_watcher_id = "directory_watcher_" + uuid.uuid4().hex
        easy_file_watcher_units = EasyFileWatcher.__get_all_easy_file_watcher_units(
            directory_path=directory_path, directory_watcher_id=directory_watcher_id)
        with EasyFileWatcherUoW() as uow:
            uow.easy_file_watcher_repository.add_all(
                easy_file_watcher_units=easy_file_watcher_units)
            uow.commit()
        workflow_scheduler.add_job(EasyFileWatcher.execute_job, 'interval',  [directory_watcher_id, directory_path, callback, callback_param, event_on_deletion], seconds=2,
                                   replace_existing=True, id=directory_watcher_id)

    @staticmethod
    def execute_job(*args):
        """This method executes the call back of the directory of interest to watch."""
        file_watcher_units_in_db = EasyFileWatcher.__get_all_current_filewatcher_units_by_directory_watcher_id(
            args[0])
        file_watcher_units = EasyFileWatcher.__get_all_easy_file_watcher_units(
            args[1], args[0])
        confirmed_change = EasyFileWatcher.__detect_change(
            old_file_watcher_units=file_watcher_units_in_db, new_file_watcher_units=file_watcher_units, event_on_deletion=args[4])
        if confirmed_change:
            args[2](**args[3])
            with EasyFileWatcherUoW() as uow:
                [uow.easy_file_watcher_repository.delete(
                    easy_file_watcher) for easy_file_watcher in file_watcher_units_in_db]
                uow.commit()
                uow.easy_file_watcher_repository.add_all(file_watcher_units)
                uow.commit()

    @staticmethod
    def __detect_change(old_file_watcher_units: List[EasyFileWatcherUnit], new_file_watcher_units: List[EasyFileWatcherUnit], event_on_deletion: bool) -> bool:
        """This method detects changes in the directory of interest to watch."""
        if event_on_deletion:
            if len(old_file_watcher_units) > len(new_file_watcher_units):
                return True
        if len(new_file_watcher_units) != len(old_file_watcher_units) or sorted(old_file_watcher_units) != sorted(new_file_watcher_units):
            return True
        return False
