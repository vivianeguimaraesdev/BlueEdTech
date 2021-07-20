/**
 * Primeiro vamos pegar todas as referências que precisamos lá do HTML
 */
const containerElement = document.querySelector('.container');
const formElement = document.querySelector('form');
const inputElement = document.querySelector('input[type=text]');

/**
 * Agora vamos adicionar event listeners para ouvir quando o usuário apertar o submit
 */
formElement.addEventListener('submit', function(e) {

    /**
     * Para que a página não reinicie
     */
    e.preventDefault();

    /**
     * Vamos limpar a div para que quando fizermos uma busca um novo
     * pokémon apareça no lugar do outro, de inicio ela já vai estar limpa
     * então não há problema em fazer essa limpeza
     */
    containerElement.innerHTML = '';

    /**
     * Por fim vamos usar o método getPokemon onde passamos o conteúdo digitado
     * na busca, essa fnução vai buscar os dados e renderizar na dela
     */
    getPokemon(inputElement.value);
});

/**
 * Nessa funcao iremos passar um nome de um pokemon, ela e assincrona
 * visto que temos que esperar toda a requisicao finailizar
 */
async function getPokemon(name) {
    /**
     * Primeiro vamos converter o nome passado para a funcao
     * para que todas as letras estejam usando caixa baixa,
     * visto que a API so aceita nomes usando letras minusculas
     * 
     */
    name = name.toLocaleLowerCase();
    
    /**
     * Fazemos uma requisicaousando a api fetch para buscar os dados
     * usamos o await para esperar ate que finalize a requisicao toda
     */
    const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`);

    /**
     * feito isso esperamos o json da requiscao e armazenamos na const pokemon
     */
    const pokemon = await res.json();

    /**
     * Feito isso iremos criar uma div para informar as informacoes
     * e depois adicionamoos a classe pokemon nessa div
     */
    const pokemonElement = document.createElement("div");
    pokemonElement.classList.add("pokemon");

    /** Agora iremos adicionnar a imagem nessa div usando o innerHtmle o appendChild */
    pokemonElement.innerHTML = `

    
    <div class="card">
        <h2>${pokemon.name[0].toUpperCase() + pokemon.name.substring(1)}</h2>
        ${
            pokemon.stats.map(
                function(item) {
                    return `
                        <p>${item.stat.name}: ${item.base_stat}</p>
                    `;
                }
            ).join("")
        }
    </div>
    
    
    <img src="https://pokeres.bastionbot.org/images/pokemon/${pokemon.id}.png" />
    `;

    /** Adicionamos esse trecho longo de html na nossa página
     * especificamente no nosso pokemonElement que é uma div que criamos anteriormente
     */
    containerElement.appendChild(pokemonElement);

}