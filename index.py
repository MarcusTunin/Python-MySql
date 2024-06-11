import mysql.connector # type: ignore

try:
    # fazer a conexao com o banco de dados
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="teste"
    )

    if connection.is_connected():
        print("conectado ao MySQL na database: " + connection.database)

    # cursor para executar o sql series
    cursor = connection.cursor()

    # comando para inserir os dados na tabela
    insert_query = "INSERT INTO teste (nome, email, usuario) VALUES (%s, %s, %s)"

    # dados para inserir na tabela
    data_to_insert = ('Marcus', 'marcustunin', 'mtunin') 

    # executar o comando
    cursor.execute(insert_query, data_to_insert)

    # confirmando o comit
    connection.commit()
    print("Dados inseridos com sucesso")

except mysql.connector.Error as e:
    print("Error connecting to MySQL database:", e)

finally:
    # encerrar cursor e comunicação com o banco
    if 'cursor' in locals():
        cursor.close()
    if connection.is_connected():
        connection.close()
        print("Conexao encerrada")
