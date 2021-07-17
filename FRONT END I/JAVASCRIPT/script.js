//Definindo variáveis

/* let fruta = 'Morango';
console.log(fruta);

fruta = 3;
console.log(fruta); */

/* const cpf= 7856642385;
let salario = 1200.10;
salario = salario + 500;
cpf = cpf + 'a';

console.log(cpf);
console.log(salario); */
/* 
let numero = 80;
console.log(typeof numero); //tipo de uma variável

numero = numero + 'a'; //concatenação
console.log(numero); */

//STRING
/* let nome = 'Julinho';
document.write(nome); */

//UNDEFINED
/* let teste;
console.log(teste);
console.log(typeof teste); */

//NaN
/* let teste = 'a' / 23;
console.log(teste); */

//Boolean
/* let teste = true;
teste = false; */

//OBJETO

/* let cadastro ={
    nome: 'Isabela',
    cidade:'Blumenau',
    estado_de_nascimento: 'Goiás',
    faculdade:'UFG'
}

console.log(cadastro);
console.log(cadastro.nome);
 */

//ARRAY
/* 
let nome =['Isabela','Julinho','Frida'];
console.log(nomes);
console.log(nomes[1]); */

//Objeto dentro de objeto
/* let aluno = {
    nome: 'Pedro',
    idade: 34,
    periodo_de_aulas: 'Noturno',
    quer_trocar_de_periodo: true,
    linguagens_preferidas: ['Python','Java','JavaScript'],
    endereco:{
        rua:'Rua dos Alfeneiros',
        numero:'345',
        cidade:'Londres',
        estado:'IG'
    }
}

console.log(aluno);
console.log(aluno.linguagens_preferidas[0]);
console.log(aluno.endereco);
console.log(aluno.endereco.cidade); */

//Soma

/* let teste = 2 +2;
let teste2 = 'Isabela ' + 'gosta '+ 'de '+ 'Dota 2';

console.log(teste);
console.log(teste2); */

//Subtração
/* let teste = 10 - 2;
console.log(teste); */

//Divisão
/* let teste = 10/2; */

//Multiplicação
/* let teste = 10 * 2; */

//Resto 
/* let teste = 10 % 2;
let divisao = 11 / 5.6
console.log(teste);
console.log(divisao); */

//Funções JavaScript
//Uma função executa um trecho de código

/* function escrevenaTela(){
    let data = '16/07/2021'
    console.log('HOJE É SEXTA!!!' + data)
} //declaração da função

escrevenaTela(); //chamanado a função */

//Declarando uma variável fora da função
/* function somaNumero(valor1, valor2){
    let soma = valor1 + valor2;
    return soma;
}

let soma = somaNumero(2, 2);
console.log(soma); */

//FUNÇAÕ COM STRINGS
/* 
function criarTexto(nome, idade, profissao){
    return (
       'Olá meu nome é ' + nome + '\n' +
       'Minha idade é: ' + idade + '\n' +
       'Minha profissão é: ' + profissao
    )
}

console.log(criarTexto('Isabella', 28, 'Eng. de Software')); */

//FUNÇÕES MAIS LÓGICAS

/* function podeDirigir(idade){
    if(idade >= 18){
        return 'Pode dirigir!';
    } return 'Não pode dirigir!'; //não precisa do else
}

console.log(podeDirigir(5));
console.log(podeDirigir(22));
console.log(podeDirigir('www')); */

//FUNÇÃO COM IFS ENCADEADOS

/* function significadoNota(nota){
    if (nota >= 90 && nota <= 100){
        return 'A';
    } else if (nota >= 80 && nota < 90){
        return 'B'
    } else if (nota >= 0 && nota < 80){
        return 'C'
    } else {
        return 'Nota inválida'
    }
}

console.log(significadoNota(0));
console.log(significadoNota(101)); */

//USANDO WHILE - VALIDAÇÃO DE SENHA

/* let senhaCadastrada = 'Chocolate#02'
let senhaDigitada = prompt("Qual a sua senha?"); //prompt abre uma janela no navegador

while(senhaDigitada  !=  senhaCadastrada){
    senhaDigitada = prompt("Senha inválida. Digite novamente!");
}

document.write('Senha correta!'); */

//USANDO O FOR
//x = 0 - onde começa
//x > 10 onde termina
// x = x++ até aonde vai 
//x++ é o mesmo que x = x + 1
//x-- é o mesmo que x = x--
/* for(let x = 10; x > 0; x = x--){
    console.log(x);
}
 */

/* for(let i = 1; i <= 10; i++){
    for(let j = 1; j <= 10; j++){
        document.write(i + 'x' + j + '=' + (i * j) + '<br >' )
    }
    document.write('<hr />') //gera linha
}

let numeros = 
[
    [30, 45, 67, 32, 12],
    [23, 45, 23, 23, 12]
] */

//FORMA MAIS INTELIGENTE DE DECLARAR UM ARRAY COM SUB ARRAYS
/* 
let alunos = ['Isabella', 'Fran', 'Frida', 'Kiara', 'Bernadette'];

let tamanho = alunos.length; //descobrir o tamanho do array
console.log(tamanho);

//Usando Arrow Function
//() => {}
//O map imprime as strings
//A arrow function é para ajudar a imprimir o map
alunos.map((item) =>{
    console.log('Nome do aluno: ' +item)
}) */

//OUTRO EXEMPLO 
//Arrow function é para simplificar a função

let numeros = [1, 3, 56, 34, 2]

numeros.map((item) =>{
    console.log(item * 2);
})