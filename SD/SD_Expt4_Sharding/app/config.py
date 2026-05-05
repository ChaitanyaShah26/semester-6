import mysql.connector
from pymongo import MongoClient

# --- SQL Config ---
SQL_CONFIG = {"host": "localhost", "user": "root", "password": "pass@123"} # Update pass

def get_sql_conn(db_name="company_main"):
    return mysql.connector.connect(**SQL_CONFIG, database=db_name)

# --- NoSQL Config ---
mongo_client = MongoClient("mongodb://localhost:27017/")
nosql_main_db = mongo_client["company_main"]["users"]

def get_nosql_shard_col(dept):
    return mongo_client[f"shard_{dept.lower()}"]["users"]