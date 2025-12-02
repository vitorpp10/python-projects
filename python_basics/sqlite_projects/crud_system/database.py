import sqlite3

DB_NAME = 'funcionarios.db'

def criar_tabela():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_funcionario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_funcionario(nome):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tb_funcionario (nome) VALUES (?)', (nome,))
    conn.commit()
    conn.close()

def listar_funcionarios():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tb_funcionario')
    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios

def atualizar_funcionario(id, novo_nome):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE tb_funcionario SET nome=? WHERE id=?', (novo_nome, id))
    conn.commit()
    conn.close()

def excluir_funcionario(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tb_funcionario WHERE id=?', (id,))
    conn.commit()
    conn.close()

