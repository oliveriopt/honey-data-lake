from tools.data_connection.source_manager import Connector
from db_interface.src.create_query import BuildInjectQuery


class InterfaceDatabase:

    def __init__(self, connector: Connector, table: str, list_values: list):
        self.conn = connector
        self.table = table
        self.list_values = list_values
        self.query = ""

    def connect_database(self):
        """
        Connection to database
        :return:
        """
        self.conn.open_connection()

    def create_insert_query(self):
        """
        Create the query for insert values
        :param table: name of the table to insert values
        :param list_values: list of values to insert
        :return:
        """
        build = BuildInjectQuery()
        self.query = build.build_query_insert(table=self.table, key_duplicate=True, list_values=self.list_values)

