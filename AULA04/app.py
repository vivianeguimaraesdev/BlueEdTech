from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index():
    nome = "Marcio"
    idade = 15
    if idade >= 18:
        maiordeidade=True
    else:
        maiordeidade = False
    cidade = "São Paulo"
    imagem = "/static/logoblue.gif"
    return render_template('index.html',nome=nome, idade=idade, cidade=cidade, imagem=imagem, maiordeidade=maiordeidade)

if (__name__ == "__main__"):
    app.run(debug= True)
