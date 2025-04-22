import datetime
from data.conexao import Conexao


class Request:

    def realizar_request(request):
        tempo = datetime.datetime.today()

        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True)

        sql = "INSERT INTO tb_requests(pedido,tempo) VALUES(%s,%s);"
        valores=(request,tempo)

        cursor.execute(sql,valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def recuperar_request():
        conexao = Conexao.criar_conexao()
        cursor=conexao.cursor(dictionary=True)
        sql="select pedido,tempo from tb_requests ORDER BY tempo DESC LIMIT 1;"
        cursor.execute(sql)
        resultado=cursor.fetchone()

        cursor.close()
        conexao.close()
        
        return resultado