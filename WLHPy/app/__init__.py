import os
from pathlib import Path
from WLHPy.data import globals as data_globals
from WLHPy.app import globals as app_globals
from WLHPy import data as mod_data


def check_first_run():
    mod_data.database_file()
    if not data_globals.db_file.exists():
        mod_data.new_database()
