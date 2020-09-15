from tools.data_connection.source_manager import Connector
from db_interface.src.interface_database import InterfaceDatabase
import db_interface.src.cons_database as cons

table_str = 'language_identification'
l_values = [("0", "ES", "FR", "DE", "EN"), ("1", "EN", "DE", "FR", "ES")]
conn_db = Connector(user=cons.user, pw=cons.pwd, host=cons.host, port=cons.port, database=cons.database)
db = InterfaceDatabase(connector=conn_db, table=table_str, list_values=l_values)
db.connect_database()
db.create_insert_query()
print(db.query)