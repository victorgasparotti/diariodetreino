import sqlite3

conexao=sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS treinos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exercicio TEXT NOT NULL,
    series INTEGER NOT NULL,
    repeticoes INTEGER NOT NULL,
    peso REAL NOT NULL,
    data TEXT NOT NULL
    )
''')
conexao.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_usuario TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
    )
''')
conexao.commit()

conexao.close()
