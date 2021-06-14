from flask import Flask
from bp import bp

app = Flask(__name__)
app.register_blueprint(bp)

if (__name__ == "__main__"):
    app.run(debug=True)

#python -m flask run -> não estiver no modo debug
#python app.py -> estiver no modo debug ; a diferença é que você pode parar a execução sempre que quiser modificar algo
#blueprint - serve para tornar a página modular; Juntar os arquivos em um só e depois importá-los e chamá-lo nas outras
#render template - trás uma página html dentro de uma roda para rodar no navegador com python
