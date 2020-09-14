import database_connection.src.cons_database as cons
from tools.data_connection.source_manager import Connector


class InterfaceDatabase:

    def __init__(self, connector: Connector):
        self.conn = connector

    def connect_database(self):
        self.conn.open_connection()


db = InterfaceDatabase(Connector(user=cons.user, pw=cons.pwd, host=cons.host, port=cons.port, database=cons.database))
db.connect_database()