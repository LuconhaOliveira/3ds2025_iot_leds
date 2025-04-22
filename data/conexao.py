import mysql.connector

class Conexao:

    # def criar_conexao():
    #     conexao = mysql.connector.connect(
    #     host="localhost", 
    #     port=3306, 
    #     user="root", 
    #     password="root", 
    #     database="db_request"
    #     )
    #     return conexao

    def criar_conexao():
        conexao = mysql.connector.connect(
        host="ds3-2025-iot-leds-aluno-d374.b.aivencloud.com", 
        port=28179, 
        user="avnadmin", 
        password="AVNS_UQtCVbBpK2Bud9cV22F", 
        database="db_request"
        )
        return conexao
