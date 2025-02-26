import os
import logging
from pymilvus import connections, db, MilvusClient, MilvusException
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.host = os.getenv("host")
        self.port = os.getenv("port")
        self.protocoll = os.getenv("protocoll")
        

config = Config()


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s |%(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs/app.log')  # Datei für Logs angeben
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)



def connect_db(db_name):
    try:
        client = MilvusClient(f"{config.protocoll}://{config.host}:{config.port}", db_name=db_name)
        logger.info(f"Connected to the database {db_name}")
    except MilvusException as e:
        logger.warning(f"Server not reachable. Please check the connection. {str(e)}")
        return None
    return client


connect_db("rag_database")