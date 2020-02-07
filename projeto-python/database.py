import sqlite3

conn = sqlite3.connect('UserData.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    NOME TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    USUARIO TEXT NOT NULL,
    SENHA TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados")