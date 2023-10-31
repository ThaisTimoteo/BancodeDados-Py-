import sqlite3

def create_db(data_base:str):
    """Create a database 

    Args:
        data_name (str): A database's name
    """
    sqlite3.connect('example.db')