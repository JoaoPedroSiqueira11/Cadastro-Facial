import sqlite3

def criar_tabelas():
    conn = sqlite3.connect("faces.db")
    cursor = conn.cursor()

    # Criar tabela de usuários
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        encoding BLOB,
                        imagem BLOB)''')

    # Criar tabela de histórico de logins
    cursor.execute('''CREATE TABLE IF NOT EXISTS historico_logins (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario_id INTEGER,
                        nome TEXT,
                        data_hora TEXT,
                        FOREIGN KEY(usuario_id) REFERENCES usuarios(id))''')

    conn.commit()
    conn.close()
