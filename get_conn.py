import sqlite3

def get_conn():
    conn = sqlite3.connect("./instance/database.db")
    #permite acessar valores por nome da coluna.
    conn.row_factory = sqlite3.Row
    return conn