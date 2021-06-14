from flask import Blueprint, render_template

bp = Blueprint('bp',__name__)

@bp.route("/")
def home():
    return "<h1>Hello, Flask! Tudo bem?</h1>"

@bp.route("/login/<nome>")
def login (nome=None):
    return "<center><h1>Olá, "+nome+"! <br />Faça seu login</center></h1>"

@bp.route("/codelab2/")
def carrega():
    return render_template('aula2_ex1_v2.html')

@bp.route("/clientes/")
def clientes():
    return"<h1> Home CLIENTES</h1>"

@bp.route("/produtos/")
def produtos():
    return"<h1>Home PRODUTOS</h1>"

@bp.route("/contato/")
def contato():
    return"<h1> Home CONTATO</h1>"
