import sqlite3

def insert_one_row(
    database_name:str,
    table_name:str,
    columns_name:str,
    values:str
) -> None:

    """Create a table on a specific database

    Args:
        database_name (str): A database's name.
        table_name (str): A table's name.
        columns (str): A query specifying the columns.
        columns_name(str): Columns to insert the valiues.
        values (str): Values to insert.

    Example: 
    insert_one_row("test.db", "tabela", "id, name, age", "30, 'samuel', 40")
    """

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO {table_name} ({columns_name}) VALUES ({values})
    """)

    conn.commit()
    conn.close()
###################################

def insert_many_rows(
    database_name:str,
    table_name:str,
    columns_name:str,
    values_list:list
) -> None:
    """Insert many rows in a table

    Args:
        database_name (str): A database's name.
        table_name (str): A table's name.
        columns (str): A query specifying the columns.
        columns_name(str): Columns to insert the valiues.
        values (str): Values to insert.
    """

    conn = sqlite3.connect('database_name')
    cursor = conn.cursor()

    query = f"INSERT INTO {table_name} ({columns_name}) VALUES (?, ?, ?)"

    cursor.executemany(query, values_list)

    conn.commit()
    conn.close()
