from flask import Flask, render_template, request
from Algoritmo_com_API_IA import gerar_texto

app = Flask(__name__)

@app.route("/")  # define a rota principal
def home(): #irá gerar uma tela no navegador
    return render_template("home.html") #isto é o que será reetornado na tela do navegador

@app.route("/gerar", methods=["POST"])
def gerar():
    entrada_usuario = request.form["entrada"]  # pega o texto do HTML
    resultado = gerar_texto(entrada_usuario)   # chama sua API
    return render_template("home.html", resposta=resultado) # O argumento "resposta=resultado" eu estou pedindo para ele imprimir o resultado na minha tela principal


if __name__ == "__main__":
    app.run(debug=True) #inicia o servidor local com reload automático ao salvar mudanças.
    