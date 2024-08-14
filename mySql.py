import mysql.connector

setConnection = mysql.connector.connect(
    host = "localhost",
    user = "user_name",
    password = "password",
    database = "database_name"

)

cursor = setConnection.cursor()

cursor.execute('''CREAT TABLE IF NOT EXIST livros (
               id INT AUTIO_INCREMENT PRIMARY KEY,
               titulo VARCHAR(255),
               autor VARCHAR(255),
               ano_publicacao INT,
               genero VARCHAR(100),
               preco DECIMAL(10,2))
''')

def adicionar_livros(titulo, autor, ano_publicacao, genero, preco):
    sqladd = '''
    INSERT INTO livros (titulo, autor, ano_publicacao, genero,preco)
    VALUES (%s, %s, %s, %s, %s)
'''

    valores = (titulo, autor, ano_publicacao, genero, preco)

    cursor.execute(sqladd, valores)
    setConnection.commit()
    print("Livro adicionado com sucesso!")