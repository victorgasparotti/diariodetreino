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
colunas = cursor.execute("PRAGMA table_info(treinos)").fetchall()
nomes_das_colunas = [coluna[1] for coluna in colunas]

print("Usuários:", cursor.execute(
    "SELECT id, nome_usuario FROM usuarios"
).fetchall())

print("Treinos sem usuário:", cursor.execute(
    "SELECT id, exercicio, usuario_id FROM treinos WHERE usuario_id IS NULL"
).fetchall())

cursor.execute(
    '''
    UPDATE treinos
    SET usuario_id = (SELECT id FROM usuarios WHERE nome_usuario = ?)
    WHERE usuario_id IS NULL
    ''',
    ('victorgasparotti@gmail.com',)
)
conexao.commit()

conexao.close()
