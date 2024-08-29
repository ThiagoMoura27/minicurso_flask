import sqlite3

# Nome do banco de dados
DATABASE = 'agenda.db'

# Conectar ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect(DATABASE)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela "pessoa" (se ainda não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoa (
        idpessoa INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Inserir 5 contatos iniciais
contatos_iniciais = [
    ('Maria Silva', '9999-1234', 'maria.silva@email.com'),
    ('João Souza', '9999-5678', 'joao.souza@email.com'),
    ('Ana Oliveira', '9999-8765', 'ana.oliveira@email.com'),
    ('Carlos Pereira', '9999-4321', 'carlos.pereira@email.com'),
    ('Fernanda Costa', '9999-5432', 'fernanda.costa@email.com')
]

# Inserir os contatos no banco de dados
cursor.executemany('''
    INSERT INTO pessoa (nome, telefone, email) 
    VALUES (?, ?, ?)
''', contatos_iniciais)

# Salvar as mudanças
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

print("Banco de dados criado com sucesso!")
