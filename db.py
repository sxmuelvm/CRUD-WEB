import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="sakura.proxy.rlwy.net",
        port=28130,
        user="root",
        password="LMgzXfUGWHJTBODdBPizEHfZIgtDYKFy",
        database="railway"
    )