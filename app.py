from flask import Flask,render_template,redirect,jsonify
from model.controller_request import Request

app = Flask(__name__)

@app.route("/")
def pagina_principal(fotoresistor=500):
    if fotoresistor >500: 
        estado_luz = "ligadas"
    else:
        estado_luz = "desligadas"
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

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)