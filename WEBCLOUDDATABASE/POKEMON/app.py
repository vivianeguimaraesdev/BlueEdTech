from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # pokemons = [
    #     {
    #         'numero': '001',
    #         'nome': 'Bulbasaur'
    #     },
    #     {
    #         'numero': '002',
    #         'nome': 'Ivysaur'
    #     },{
    #         'numero': '003',
    #         'nome': 'Venusaur'
    #     },{
    #         'numero': '004',
    #         'nome': 'Charmander'
    #     },{
    #         'numero': '005',
    #         'nome': 'Charmeleon'
    #     },{
    #         'numero': '006',
    #         'nome': 'Charizard'
    #     },{
    #         'numero': '007',
    #         'nome': 'Squirtle'
    #     },{
    #         'numero': '008',
    #         'nome': 'Wartortle'
    #     },{
    #         'numero': '009',
    #         'nome': 'Blastoise'
    #     },{
    #         'numero': '010',
    #         'nome': 'Caterpie'
    #     },{
    #         'numero': '011',
    #         'nome': 'Metapod'
    #     },{
    #         'numero': '012',
    #         'nome': 'Butterfree'
    #     },
    # ]
    pokemons = [
        {'numero':'001', 'nome':'Bulbasaur'},
        {'numero':'002', 'nome':'Ivysaur'},
        {'numero':'003', 'nome':'Venusaur'},
        {'numero':'004', 'nome':'Charmander'},
        {'numero':'005', 'nome':'Charmeleon'},
        {'numero':'006', 'nome':'Charizard'},
        {'numero':'007', 'nome':'Squirtle'},
        {'numero':'008', 'nome':'Wartortle'},
        {'numero':'009', 'nome':'Blastoise'},
        {'numero':'010', 'nome':'Caterpie'},]
    caminho_base = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'

    return render_template("index.html", pokemons=pokemons, caminho_base=caminho_base)

if (__name__ == "__main__"):
    app.run(debug=True)