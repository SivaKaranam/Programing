"""
Script for connecting to ZINKA DB's
"""

import MySQLdb

from auto_input import (db_host,
    db_user,
    db_password,
    db_name)

class MyDB(object):
    """
    Db connections starts here.
    """
    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = MySQLdb.connect(db_host, db_user,
            db_password, db_name)
        self._db_cur = self._db_connection.cursor()

    def query(self, qry, vals):
        """ Executes the given query """
        self._db_cur.execute(qry, vals)

    def __del__(self):
        self._db_connection.close()
        self._db_cur.close()

    def main(self, qry, vals):
        """ Main """
        self.query(qry, vals)
