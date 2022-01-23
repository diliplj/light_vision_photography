# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
from pathlib import Path
from django.conf import settings

import os
from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photography_jan_6.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'photography_jan_6.settings'

application = get_wsgi_application()


import app_logger
import app_lifecycle_api

log_name = "app_scripts"
logger = app_logger.createLogger(log_name)

#@app_logger\.functionlogs\(log=log_name\)
def init():
    app_lifecycle_api.dropDatabase()
    app_lifecycle_api.createDatabase()
    app_lifecycle_api.migrate_app_database()
    load_data()
    create_super_user()


#@app_logger\.functionlogs\(log=log_name\)
def load_data():
    app_lifecycle_api.run_fixtures()


#@app_logger\.functionlogs\(log=log_name\)
def create_super_user():
    app_lifecycle_api.create_super_user()


if __name__ == '__main__':
    POSSIBLE_COMMANDS_LIST = ["init", "loaddata", "create_super_user"]
    if len(sys.argv) < 2:
        sys.exit("""Must provide args like \n\t %s"""%("\n\t ".join(POSSIBLE_COMMANDS_LIST)))
    else:
        if sys.argv[1] in POSSIBLE_COMMANDS_LIST:
            # print("Starting: %s" % (sys.argv[1]))
            print("Starting: %s" % (sys.argv[1]))
            if sys.argv[1] == 'init':
                init()
            elif sys.argv[1] == 'loaddata':
                load_data()
            elif sys.argv[1] == 'create_super_user':
                create_super_user()
            else:
                print("""Invalid argument, Must provide args like \n\t %s"""%("\n\t ".join(POSSIBLE_COMMANDS_LIST)))
            print("Done...")
        else:
            sys.exit("""Invalid argument, Must provide args like \n\t %s"""%("\n\t ".join(POSSIBLE_COMMANDS_LIST)))
