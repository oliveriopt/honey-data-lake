from tools.data_connection.source_manager import Connector
from db_interface.src.interface_database import InterfaceDatabase
from db_interface.src.create_query import BuildInjectQuery

import pandas as pd
import os
import db_interface.src.cons_database as cons
import sys
sys.setrecursionlimit(20000)

class InjectData:
    """
    INJECT DATA TO POSGRES SQL DATABASE
    """
    def __init__(self, path_file: str):
        self.file = path_file
        self.l_values = []
        self.conn_db = Connector(user=cons.user, pw=cons.pwd, host=cons.host, port=cons.port, database=cons.database)

    def read_csv_file(self) -> pd.DataFrame:
        """
        Read csv file
        :return:
        """
        df = pd.read_csv(self.file, index_col=0)
        records = df.to_records(index=True)
        self.l_values = list(records)

    def connect_insert_query(self, table: str):
        """
        Connect and insert the data to database
        :param table:
        :return:
        """
        db_interface = InterfaceDatabase(connector=self.conn_db, table=table, list_values=self.l_values)
        db_interface.connect_database()
        db_interface.create_insert_query()
        self.conn_db.insert_query(db_interface.query)

    def connect_select_query(self):
        build = BuildInjectQuery()
        query = build.build_query_select("persona", "geographic_zone")



file_table = "persona"

os.chdir("../..")
path = os.getcwd()
inject = InjectData(path + "/data/data_normalization/" + file_table + ".csv")
inject.read_csv_file()
inject.connect_insert_query(file_table)

#inject.connect_select_query()
