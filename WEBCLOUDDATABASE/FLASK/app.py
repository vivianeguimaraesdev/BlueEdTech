from flask import Flask

app = Flask(__name__) #criando um objeto flask para essa aplicação corrente

@app.route("/") #a barra dentro do parenteses é o endereço. URL.
def hello_world():
    return "<h1>Hello, Flask! Olha a T2C3 na área!</h1>" #string com instrução em html

if (__name__ == "__main__"):
    app.run(debug=True)
