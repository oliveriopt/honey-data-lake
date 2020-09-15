from tools.data_connection.source_manager import Connector
from pypika import Query, Table, Field

import database_connection.src.cons_database as cons


class InterfaceDatabase:

    def __init__(self, connector: Connector):
        self.conn = connector

    def connect_database(self):
        """
        Connection to database
        :return:
        """
        self.conn.open_connection()

    def create_insert_query(self, table, values):
        customers = Table(table)

     #   q = Query.into(table).insert(1, 'Jane', 'Doe', 'jane@example.com') \
     ##       .on_conflict(customers.email)
     #   .do_update(customers.email, 'bob@example.com')


conn_db = Connector(user=cons.user, pw=cons.pwd, host=cons.host, port=cons.port, database=cons.database)
db = InterfaceDatabase(connector= conn_db)
db.connect_database()