//Primeiro criar uma viarável para linkar com o html
//pokemonapi.co

const elementoContainer = document.querySelector('.container');
const elementoFormulario = document.querySelector('form');
const elementoInput = document.querySelector('input[type=text]');

elementoFormulario.addEventListener('submit', function(e){
    e.preventDefault();

    elementoFormulario.innerHTML = '';

    pegarPokemon(elementoInput.value);
});

 async function pegarPokemon(nome){
    nome = nome.toLowerCase();

    const resposta = await fetch(`https://pokeapi.co/api/v2/pokemon/${nome}`);
    
    const pokemonInfo = await resposta.json();
    
    const elementoPokemon = document.createElement("div");
    elementoPokemon.classList.add("pokemon"); //criando uma div com uma classe

    elementoPokemon.innerHTML = `
        <div class="card">
            <h2>${pokemonInfo.name[0].toUpperCase() + pokemonInfo.name.substring(1)}</h2>
             ${
                pokemonInfo.stats.map(
                    function(item){
                        return `<p> ${item.stat.name}: ${item.base.stat}</p>`
                    }
                ).join(" ")
             }
        </div>
        <img src="https://pokeres.bastionbot.org/images/pokemon/${pokemonInfo.id}.png" />
    `;

    //Depois de tudo adicionar a div dentro do container
    elementoContainer.appendChild(elementoPokemon);
}

//Await espera algo chegar, para iniciar 
