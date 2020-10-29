from tools.data_connection.source_manager import Connector
from src.db_interface.create_query import BuildInjectQuery


class InterfaceDatabase:

    def __init__(self, connector: Connector, table: str or None, list_values: list or None, select_table: str or None,
                 select_table_join: str or None, select_table_join_2: str or None, select_table_join_3: str or None):
        self.conn = connector
        self.table = table
        self.list_values = list_values
        self.query = ""
        self.select_table = select_table
        self.select_table_join = select_table_join
        self.select_table_join_2 = select_table_join_2
        self.select_table_join_3 = select_table_join_3

    def connect_database(self):
        """
        Connection to database
        :return:
        """
        self.conn.open_connection()

    def create_insert_query(self) -> None:
        """
        Create the query for insert values
        :param table: name of the table to insert values
        :param list_values: list of values to insert
        :return:
        """
        build = BuildInjectQuery()
        self.query = build.build_query_insert(table=self.table, key_duplicate=True, list_values=self.list_values)

    def create_select_query(self, limit:int, offset:int) -> None:
        """
        Create select query
        :param limit:
        :param offset:
        :return:
        """
        build = BuildInjectQuery()
        self.query = build.build_query_select(self.select_table, self.select_table_join, self.select_table_join_2,
                                              self.select_table_join_3, limit=limit, offset=offset)
