import dao

conn = dao.connect_db()

#CRIANDO A TABELA DOS COLABORADORES 
conn.execute('CREATE TABLE colaboradores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, funcao TEXT)')

#INSERINDO DADOS PARA TESTES
conn.execute("INSERT INTO colaboradores (nome,funcao) VALUES ('CELSO','ENCARREGADO')")
conn.execute("INSERT INTO colaboradores (nome,funcao) VALUES ('DAN', 'ENCARREGADO')")
conn.execute("INSERT INTO colaboradores (nome,funcao) VALUES ('REUEL', 'ENCARREGADO')")
conn.execute("INSERT INTO colaboradores (nome,funcao) VALUES ('ARMANDO', 'OFICIAL')")
conn.execute("INSERT INTO colaboradores (nome,funcao) VALUES ('MANFRED', 'OFICIAL')")
conn.execute("INSERT INTO colaboradores (nome,funcao) VALUES ('SHARIF', 'OFICIAL')")
conn.execute("INSERT INTO colaboradores (nome,funcao) VALUES ('CECILIO', 'AJUDANTE')")
conn.execute("INSERT INTO colaboradores (nome,funcao) VALUES ('LOURENCO', 'AJUDANTE')")
conn.execute("INSERT INTO colaboradores (nome,funcao) VALUES ('PEDRO', 'AJUDANTE')")


#CRIANDO A TABELA DE SERVICO
conn.execute('CREATE TABLE servicos (id INTEGER PRIMARY KEY AUTOINCREMENT, ordem_de_servico INTEGER, cliente TEXT, endereco, lat INTEGER, long INTEGER)')

#INSERINDO MANUALMENTE O DADO PARA TESTE
# "R. Capote Valente, 39 - Pinheiros, São Paulo - SP, 05409-000"
conn.execute("INSERT INTO servicos (ordem_de_servico, cliente, endereco) VALUES (336, 'Carolina Rosângela Almeida', 'AV. SENADOR PINHEIRO MACHADO 475, MARAPE SANTOS-SP - 11075000')")
conn.execute("INSERT INTO servicos (ordem_de_servico, cliente, endereco) VALUES (135, 'Ed. Mariane Gomes', 'Rua Amador Bueno, 768 - Centro,  Santos-SP, 11013153')")
conn.execute("INSERT INTO servicos (ordem_de_servico, cliente, endereco) VALUES (541, 'Pedro Hugo Brito', 'Praça Dutra Vaz, 753 - Vila Mathias, Santos/SP, 11075180')")


#CRIANDO A TABELA EQUIPE 
conn.execute("""CREATE TABLE equipe (id INTEGER PRIMARY KEY AUTOINCREMENT, ordem_de_servico INTEGER, 
encarregado TEXT, oficial TEXT, ajudante TEXT)""")

conn.commit()

