from flask import Flask,render_template,redirect,jsonify
from model.controller_request import Request

app = Flask(__name__)

estado_luz = 0

@app.route("/")
def pagina_principal():
    global estado_luz
    return render_template("index.html",estado_luz=estado_luz)

@app.route("/led/ligar")
def ligar_led():
    Request.realizar_request("1")
    return redirect("/")

@app.route("/led/desligar")
def desligar_led():
    Request.realizar_request("0")
    return redirect("/")

@app.route("/request")
def request():
    return jsonify(Request.recuperar_request())

@app.route("/luzSala/ligar")
def ligar_luz_sala():
    global estado_luz
    estado_luz = "ligadas"
    return "ligou"

@app.route("/luzSala/desligar")
def desligar_luz_sala():
    global estado_luz
    estado_luz = "desligadas"
    return "desligou"

@app.route("/get/estadoLuz")
def get_estado_luz():
    global estado_luz
    return jsonify({"estado_luz": estado_luz})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)