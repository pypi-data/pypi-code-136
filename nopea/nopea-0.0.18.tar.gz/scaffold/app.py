# This file is needed to initialize the models and migrations
import os
from nopea.dbobject import DbObject
from nopea.adaptors.sqlite import SQLiteAdaptor
from nopea.migrations import Migration

from models import *

DbObject.adaptor = SQLiteAdaptor('nopea.db')

# Examples for other DBMS

# MySQL
# from nopea.adaptors.mysql import MySQLAdaptor
# DbObject.adaptor = MySQLAdaptor({
#     'host': 'localhost',
#     'user': 'nopea',
#     'db': 'nopea',
#     'use_unicode': True,
#     'charset': 'utf8'
# })


# from nopea.adaptors.postgres import PostgreSQLAdaptor
# DbObject.adaptor = PostgreSQLAdaptor({
#     'host': 'localhost',
#     'user': 'nopea',
#     'database': 'nopea',
#     'password': 'nopea'
# })

Migration.migration_dir = os.path.join(os.getcwd(), 'migrations')
