import os
from pymilvus import connections, db
from dotenv import load_dotenv

load_dotenv()
def create_connection(db_name):
    conn = connections.connect(
    host=os.getenv("host"),
    port=os.getenv("port"),
    db_name=db_name
    )
    return conn

def create_db(db_name):
    create_connection(db_name)
    database = db.create_database(db_name)

def connect_db(db_name):
    conn = connections.connect(
    host="127.0.0.1",
    port="19530",
    db_name=db_name
)
    
connect_db("rag_db")
    