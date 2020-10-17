from tools.data_connection.source_manager import Connector
from src.db_interface.interface_database import InterfaceDatabase

import pandas as pd
import src.db_interface.cons_database as cons
import sys

sys.setrecursionlimit(20000)


class SelectInsertUpdateDataSQL:
    """
    INJECT DATA TO POSGRES SQL DATABASE
    """

    def __init__(self, path_file: str or None, insert_table: str or None, insert_values: list or None, select_table:
    str or
                                                                                                             None,
                 select_join_table: str or None):
        self.path_file = path_file
        self.insert_table = insert_table
        self.insert_values = insert_values
        self.select_table = select_table
        self.select_join_table = select_join_table
        self.conn_db = Connector(user=cons.user, pw=cons.pwd, host=cons.host, port=cons.port, database=cons.database)

    def __read_csv_file(self) -> None:
        """
        Read csv file
        :return:
        """
        df = pd.read_csv(self.path_file, index_col=0)
        records = df.to_records(index=True)
        self.insert_values = list(records)
        print(self.insert_values)

    def __connect_insert_query(self) -> None:
        """
        Connect and insert the data to database
        :param table:
        :return:
        """
        db_interface = InterfaceDatabase(connector=self.conn_db, table=self.insert_table,
                                         list_values=self.insert_values,
                                         select_table=None, select_join_table=None)
        db_interface.connect_database()
        db_interface.create_insert_query()
        self.conn_db.insert_update_query(db_interface.query)

    def __connect_select_query(self) -> tuple:
        """
        Select query and returh the data on list of tuples
        :param select_table:
        :param select_join_table:
        :return:
        """
        db_interface = InterfaceDatabase(connector=self.conn_db, table=None, list_values=None,
                                         select_table=self.select_table, select_join_table=self.select_join_table)
        db_interface.connect_database()
        db_interface.create_select_query()
        return self.conn_db.select_query(db_interface.query)

    def process_inject_query_using_file(self) -> None:
        """
        Process Insert/Update query
        :param path:
        :param file_table:
        :return:
        """
        self.__read_csv_file()
        self.__connect_insert_query()

    def process_update_query(self) -> None:
        """
        Process Insert/Update query
        :param path:
        :param file_table:
        :return:
        """
        self.__connect_insert_query()

    def process_select_query(self) -> None:
        """
        Process select query
        :return:
        """
        self.__connect_select_query()
