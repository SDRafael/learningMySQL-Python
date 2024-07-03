import mysql.connector
# setando a conexão com o BD
conexao = mysql.connector.connect(host='host_adress',database='db_name',user='user_name',password='password')

# imprimindo a confirmação de conexão e estabelecendo o cursor
if conexao.is_connected():
    print('conectado com sucesso')
    cursor = conexao.cursor()

idade = int(input())

if idade >= 18:
    productName = input()
    productValue = float(input())

    cursor.execute(f'insert into vendas(produto, preço) value ("{productName}",{productValue});')
    conexao.commit()
else:
    cursor.execute('SELECT * FROM vendas where preço < 100;')
    read = cursor.fetchall()
    print(read)
# lembrar de sempre fechar as conexões independente dos resultados
conexao.close()
cursor.close()    
