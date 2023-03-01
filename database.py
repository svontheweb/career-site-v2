import os
from sqlalchemy import create_engine
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string)



