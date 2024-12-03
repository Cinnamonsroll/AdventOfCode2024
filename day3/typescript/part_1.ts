import * as fs from 'fs';

const memory = fs.readFileSync('input.txt', 'utf8');

const regex = /mul\((\d+),(\d+)\)/g;
let result = 0;
let match: RegExpExecArray | null;

while ((match = regex.exec(memory)) !== null) {
  const x = parseInt(match[1], 10);
  const y = parseInt(match[2], 10);
  result += x * y;
}

console.log(result);
