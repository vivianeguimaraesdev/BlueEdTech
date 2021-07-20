/**
 * Here we get the element display where we're going to see the calculations
 */
let display = document.getElementById("display-screen");

/**
 * Now we declare some variables to store the first part of the expression, the second, the operation and the calculation end.
 */
let temp1;
let temp2;
let opIndex;
let operation = {
  sum: false,
  plus: false,
  divide: false,
  minus: false,
  pow: false,
  sqrt: false,
  percent: false,
  parenthesis: false,
  parenthesisIndex: []
}
let calc;
let finished = false;

/**
 * Seven key
 */
function typeSeven() {
  clean();
  display.value += 7;
}

/**
 * Eight key
 */
function typeEight() {
  clean();
  display.value += 8;
}

/**
 * Nine key
 */
function typeNine() {
  clean();
  display.value += 9;
}

/**
 * Four key
 */
 function typeFour() {
  clean();
  display.value += 4;
}

/**
 * Five key
 */
 function typeFive() {
  clean();
  display.value += 5;
}

/**
 * Six key
 */
 function typeSix() {
  clean();
  display.value += 6;
}

/**
 * One key
 */
 function typeOne() {
  clean();
  display.value += 1;
}

/**
 * Two key
 */
 function typeTwo() {
  clean();
  display.value += 2;
}

/**
 * Three key
 */
 function typeThree() {
  clean();
  display.value += 3;
}

/**
 * Zero key
 */
 function typeZero() {
  clean();
  display.value += 0;
}

/**
 * Point key
 */
 function typePoint() {
  clean();
  display.value += ".";
}

/**
 * Operations
 * Divide key
 */
function typeDivide() {
  clean();
  display.value += "÷";
  operation.divide = true;
}

/**
 * Plus key
 */
function typePlus() {
  clean();
  display.value += "x";
  operation.plus = true;
}

/**
 * Sum key
 */
 function typeSum() {
  clean();
  display.value += "+";
  operation.sum = true;
}

/**
 * Sum minus
 */
 function typeMinus() {
  clean();
  display.value += "-";
  operation.minus = true;
}

/**
 * Percent key
 */
 function typePercent() {
  clean();
  display.value += '%';
  operation.percent = true;
}

/**
 * Sqrt key
 */
 function typeSqrt() {
  clean();
  display.value += '√';
  operation.sqrt = true;
}

/**
 * Pow key
 */
 function typePow() {
  clean();
  display.value += "^";
  operation.pow = true;
}

/**
 * Left parenthesis key
 */
 function typeLeftPar() {
  clean();
  display.value += "(";
  operation.parenthesis = true;
  operation.parenthesisIndex.push(display.value.indexOf("("));
  console.log(operation.parenthesisIndex);
}

/**
 * Left parenthesis key
 */
 function typeRightPar() {
  clean();
  display.value += ")";
  operation.parenthesis = true;
  operation.parenthesisIndex.push(display.value.indexOf(")"));
  console.log(operation.parenthesisIndex);
}

/**
 * When the equals is pressed we verify the operation and get the substring of left and right and after 
 */
function calculate() {

  if(operation.divide) {
    simpleOp("÷");
  }
  else if(operation.minus) {
    simpleOp("-");
  }
  else if(operation.sum) {
    simpleOp("+");
  }
  else if(operation.plus) {
    simpleOp("x");
  }
  else if(operation.pow) {
    simpleOp('^');
  }
  else if(operation.pow) {
    simpleOp('√');
  }
  else {
    display.value = 'ERROR';
  }
}

/**
 * Erase the last character of the string
 */
function erase() {
  if(display.value != 0) {
    display.value = display.value.slice(0, display.value.length - 1);
  }
}

/**
 * Clear the display addng a zero value and also reinitilizing all variables
 */
function clearDisplay() {
  display.value = 0;
  temp1 = 0;
  temp2 = 0;
  opIndex = 0;
  operation = {
    sum: false,
    plus: false,
    divide: false,
    minus: false,
    pow: false,
    sqrt: false,
    percent: false,
    parenthesis: false,
    parenthesisIndex: []
  }
}

/**
 * When typping a new number, reset the Display
 */
function clean() {
  if(display.value == 0) {
    display.value = "";
  }
}

/**
 * Simple operation
 */
function simpleOp(operation) {
  if(operation == '√') {
    opIndex = 0;
    temp1 = parseInt(display.value.substring(opIndex + 1, display.value.length));

  } else {
    opIndex = display.value.indexOf(operation);
    temp1 = parseInt(display.value.substring(0, opIndex));
    temp2 = parseInt(display.value.substring(opIndex + 1, display.value.length));
  }
  
  if(operation == '+') {calc = temp1 + temp2}
  else if(operation == '-') {calc = temp1 - temp2}
  else if(operation == '*') {calc = temp1 * temp2}
  else if(operation == '÷') {calc = temp1 / temp2}
  else if(operation == '^') {calc = Math.pow(temp1, temp2)}
  else if(operation == '√') {calc = Math.sqrt(temp1)}
  
  if (isNaN(calc)) {
    display.value = 'ERROR';
  } else {
    display.value = calc;
  }
}
 