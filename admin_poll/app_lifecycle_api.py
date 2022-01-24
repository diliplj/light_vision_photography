# -*- coding: utf-8 -*-
#!/usr/bin/env python

# from python
import os
import sys
import glob
import MySQLdb
# from django
from django.conf import settings
from django.core.management import call_command
# from appllication
import app_logger

dbengine = settings.DATABASES['default']['ENGINE']
dbname = settings.DATABASES['default']['NAME']
dbhost = settings.DATABASES['default']['HOST']
dbuser = settings.DATABASES['default']['USER']
dbpass = settings.DATABASES['default']['PASSWORD']

from admin_poll.models import *
from admin_poll import api

log_name = "app_scripts"
logger = app_logger.createLogger(log_name)

@app_logger.functionlogs(log=log_name)
def createDatabase():
    result = False
    try:
        db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass)
        logger.debug("creating database...{0}".format(dbname))
        db.autocommit = True
        cursor = db.cursor()
        createsql = "create SCHEMA %s CHARACTER SET utf16 COLLATE utf16_general_ci" % (dbname)
        db.autocommit = True
        cursor.execute(createsql)
        cursor.close()
        db.close()
        logger.debug("created database...{0}".format(dbname))
        result = True
    except Exception as error:
        exception_traceback = sys.exc_info()
        print('Error at %s:%s' % (exception_traceback[2].tb_lineno, error))
        logger.error('Error at %s:%s' % (exception_traceback[2].tb_lineno, error))
        raise error
    return result


@app_logger.functionlogs(log=log_name)
def dropDatabase():
    result = False
    try:
        db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass)
        cursor = db.cursor()
        dropsql = 'drop SCHEMA %s' % (dbname)
        logger.debug("droping database...{0}".format(dbname))
        try:
            cursor.execute(dropsql)
        except Exception as error:
            exception_traceback = sys.exc_info()
            print('Error at %s:%s' % (exception_traceback[2].tb_lineno, error))
            logger.error('Error at %s:%s' % (exception_traceback[2].tb_lineno, error))
        cursor.close()
        db.close()
        logger.debug("dropped database...{0}".format(dbname))
        result = True
    except Exception as error:
        exception_traceback = sys.exc_info()
        print('Error at %s:%s' % (exception_traceback[2].tb_lineno, error))
        logger.error('Error at %s:%s' % (exception_traceback[2].tb_lineno, error))
        raise error
    return result


@app_logger.functionlogs(log=log_name)
def migrate_app_database():
    result = False
    try:
        app_list = [app for app in settings.INSTALLED_APPS if not app.startswith("django")]
        for apps in app_list:
            apps = apps.replace(".", "/")
            migration_path = os.path.join(settings.BASE_DIR, '/admin_poll/%s/migrations' % (apps))
            for file in glob.glob(migration_path + "/0*.py"):
                os.remove(file)

        for apps in app_list:
            if apps.startswith("SAF") or apps.startswith("SAS"):
                apps = apps.rsplit(".", 1)
                call_command('makemigrations', '--pythonpath', apps[0].replace(".", "/"), apps[1], interactive=False)

        call_command('makemigrations', interactive=False)
        call_command('migrate', interactive=False)
        result = True
    except Exception as e:
        exception_traceback = sys.exc_info()
        print('Error at %s:%s' % (exception_traceback[2].tb_lineno, e))
        logger.error('Error at %s:%s' % (exception_traceback[2].tb_lineno, e))
    return result



@app_logger.functionlogs(log=log_name)
def _load_fixture(fixture_name):
    try:
        print(fixture_name)
        logger.info("fixture_name : %s" % (fixture_name))
        call_command('loaddata', '%s' % (fixture_name), verbosity=1)
    except Exception as e:
        exception_traceback = sys.exc_info()
        print('Error at %s:%s' % (exception_traceback[2].tb_lineno, e))
        print("========================================================")
        logger.error('Error at %s:%s' % (exception_traceback[2].tb_lineno, e))


@app_logger.functionlogs(log=log_name)
def run_fixtures():
    try:
        
        apps_list = [app for app in settings.INSTALLED_APPS if not app.startswith("django")]
        for app_label in apps_list:
            app_path = "/".join(app_label.split("."))
            json_folder = os.path.join(settings.BASE_DIR, 'admin_poll', app_path, 'fixtures')
            print(json_folder)
            for fixture_name in sorted(glob.glob(json_folder + "/" + "*.json")):
                _load_fixture(fixture_name)
    except Exception as e:
        exception_traceback = sys.exc_info()
        print('Error at %s:%s' % (exception_traceback[2].tb_lineno, e))
        print("========================================================")
        logger.error('Error at %s:%s' % (exception_traceback[2].tb_lineno, e))

def create_super_user():
    try:
        user_dict = dict(first_name="dilip",
                         last_name="lj",
                         email_address="diliplj5@gmail.com",
                         password="dilip")
        request = None

        #create User
        result, user = api._user_creation_flow(request, user_dict)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.username = "dilip" 
        user.save()

        #create UserKYCProfile
        # result, user_kyc_profile = api._user_kyc_profile_creation_flow(request, user_dict, user)
        
        # #create Account
        # account_type = AccountType.objects.get(name='BUSINESS')
        # result, account = api._account_creation_flow(request, account_type, user)

        # #create AccountGroup + Group from DefaultAccountGroup
        # default_account_group = DefaultAccountGroup.objects.filter(account_type=account_type)
        # result = api._account_group_creation_flow(request, account, default_account_group, user)
        
        # #create AccountSettings from DefaultAccountSettings
        # default_account_settings = DefaultAccountSettings.objects.filter(account_type=account_type)
        # result = api._account_settings_creation_flow(request, account, default_account_settings, user)

        # #create AccountUser
        # result, account_user = api._account_user_creation_flow(request, account, user)
        
        # #create AccountUserSettings
        # account_settings = AccountSettings.objects.filter(account=account,datamode='A')
        # result = api._account_user_settings_creation_flow(request, account_user, account_settings, user)
        
        # #add User to Default Group of the Account
        # group = DefaultAccountGroup.objects.get(account_type=account_type, is_default=True).group
        # result = api._user_group_mapping_flow(request, group, user)

    except Exception as e:
        exception_traceback = sys.exc_info()
        print('Error at %s:%s' % (exception_traceback[2].tb_lineno, e))
        print("========================================================")
        logger.error('Error at %s:%s' % (exception_traceback[2].tb_lineno, e))
