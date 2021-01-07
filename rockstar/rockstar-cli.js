
// see https://github.com/RockstarLang/rockstar/tree/master/satriani

const satriani = require('../../rockstar/satriani/satriani.js');

// Required to support reading from stdin
const readlineSync = require('readline-sync');
const fs = require('fs')

const programFile = process.argv[2]
const inputFile = process.argv[3]

const program = fs.readFileSync(programFile, 'utf8')
const inputs = fs.readFileSync(inputFile, 'utf8').split(/\n/g);
const input = function() { return inputs.shift(); };

const rockstar = new satriani.Interpreter();
const ast = rockstar.parse(program);

// Draw the abstract syntax tree (AST) to the console as a JSON object
//console.log(JSON.stringify(ast, null, 2))

const output = console.log
const result = rockstar.run(ast, input, output)
if (result !== 0) {
    console.log("Error Code: " + result);
}
