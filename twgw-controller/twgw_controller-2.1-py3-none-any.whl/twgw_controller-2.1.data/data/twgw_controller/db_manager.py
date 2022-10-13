# # ******************************************************************************
# #  Copyright (c) 2020. Tracker wave Pvt Ltd.
# # ******************************************************************************
#

import logging
import os
import sqlite3
import subprocess
from datetime import datetime
from pathlib import Path
import traceback
from rich.logging import RichHandler


class SQLiteDB:
    create_gw_table = '''CREATE TABLE gateway_tracker (id INTEGER PRIMARY KEY AUTOINCREMENT, evtdt datetime, gw_id TEXT NOT NULL, pid INTEGER, exe_bundle TEXT,
        start_time datetime, stop_time datetime)'''
    table_gw_exist = "SELECT name FROM sqlite_master WHERE type='table' AND " \
                     "name='gateway_tracker'"

    def __init__(self):
        home = str(Path.home())
        self.home_path = os.path.join(str(home), "tw")
        FORMAT = "%(message)s"
        logging.basicConfig(
            level="NOTSET", format=FORMAT, datefmt="[%X]",
            handlers=[RichHandler(show_path=False, omit_repeated_times=False)]
        )
        self.log = logging.getLogger("rich")

    def create_schema_gw(self):
        try:
            self.gw_db = sqlite3.connect(self.gw_table_path)
            self.gw_cur = self.gw_db.cursor()
            if self.gw_cur.execute(self.table_gw_exist).fetchone() is None:
                self.gw_cur.execute(self.create_gw_table)
            return True
        except Exception:
            self.log.exception("Exception with creating gateway process tracker schema - " +
                               str(traceback.format_exc()))
            return False

    def insert_gw_info(self, exe_path, post_data):
        try:
            self.exe_path = exe_path
            self.gw_path = os.path.dirname(self.exe_path)
            self.gw_table_name = os.path.basename(self.gw_path)
            self.gw_table_path = os.path.join(self.gw_path, self.gw_table_name + ".db")
            self.create_schema_gw()
            cmnd = "insert into gateway_tracker(id, evtdt, gw_id, pid, exe_bundle, start_time, stop_time) " \
                   "values (null, ?, ?, ?, ?, ?, ?) "
            self.gw_cur.executemany(cmnd, post_data)
            self.gw_db.commit()
            self.gw_db.close()
            self.log.info("Successfully posted gateway information...")
            return True
        except Exception:
            self.log.exception("Exception with posting gateway process information - " + str(traceback.format_exc()))
            return False

    def update_gw_info(self, tmp_path, gw_path):
        try:
            gw_id = os.path.basename(gw_path)
            self.gw_table_path = os.path.join(gw_path, str(gw_id) + ".db")
            self.create_schema_gw()
            query = """select * from gateway_tracker where id = (select MAX(id) from gateway_tracker where gw_id=?)"""
            self.gw_cur.execute(query, (str(gw_id),))
            records = self.gw_cur.fetchall()
            if records is not None and len(records) > 0:
                temp_folder_name = records[0][4]
                table_id = records[0][0]
                temp_folder_path = os.path.join(str(tmp_path), str(temp_folder_name))
                if os.path.exists(temp_folder_path):
                    subprocess.call(["rm", "-r", temp_folder_path])
                    self.log.info("Gateway executable bundle removed safely..."+str(temp_folder_path))
                put_data = (datetime.now(), datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f'), table_id)
                self.gw_cur.execute("UPDATE gateway_tracker SET evtdt=?, stop_time=? WHERE id = ?", put_data)
                self.gw_db.commit()
                self.gw_db.close()
        except Exception:
            self.log.exception("Exception with updating gateway process information - " + str(traceback.format_exc()))

    def get_pulse(self, table, limit=None):
        try:
            query = """SELECT *  FROM """ + str(table)
            if limit is not None:
                query += """ order by id DESC LIMIT """ + str(limit)
            self.cur.execute(query)
            records = self.cur.fetchall()
            self.db.close()
            return records
        except Exception:
            self.log.exception("Exception with fetching gateway process information - " + str(traceback.format_exc()))
