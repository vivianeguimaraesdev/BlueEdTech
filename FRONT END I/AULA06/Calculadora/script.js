/*Pegando o elemento do displayp pelo ID*/

let display = document.getElementById("display-screen");

let esquerda;
let direita;
let indexDaOperacao;
let calculoFinal;
//Objeto - Operações
let operacoes = {
    soma:false,
    multiplicacao: false,
    divisao: false,
    subtracao: false,
    potencia: false,
    raiz: false,    
}

//Fazendo os botões

function digitarSete(){
    limparVisor();
    display.value = display.value + 7;
}

function digitarOito(){
    limparVisor();
    display.value = display.value + 8;
}

function digitarNove(){
    limparVisor();
    display.value = display.value + 9;
}

function digitarQuatro(){
    limparVisor();
    display.value = display.value + 4;
}

function digitarCinco(){
    limparVisor();
    display.value = display.value + 5;
}

function digitarSeis(){
    limparVisor();
    display.value = display.value + 6;
}


function digitarUm(){
    limparVisor();
    display.value = display.value + 1;
}

function digitarDois(){
    limparVisor();
    display.value = display.value + 2;
}

function digitarTrês(){
    limparVisor();
    display.value = display.value + 3;
}

function digitarZero(){
    limparVisor();
    display.value = display.value + 0;
}

//Operações

function digitarDivisao(){
    limparVisor();
    display.value = display.value + '÷';
    operacoes.divisao = true;
}

function digitarMultiplicacao(){
    limparVisor();
    display.value = display.value + 'x';
    operacoes.multiplicacao = true;
}

function digitarSubstracao(){
    limparVisor();
    display.value = display.value + '-';
    operacoes.subtracao = true;
}

function digitarSoma(){
    limparVisor();
    display.value = display.value + '+';
    operacoes.soma = true;
}




/* Limpar o display quando digitar o primeiro número */

function limparVisor(){
    if (display.value == 0){
        display.value = " ";
    }
}

function calcular(operacao){
    posicaoDaOperacao = display.value.indexOf(operacao);
    esquerda = parseInt(display.value.substring(0, posicaoDaOperacao));
    direita = display.value.substring(posicaoDaOperacao + 1, display.value.length)
}