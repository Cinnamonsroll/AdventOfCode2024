import * as fs from 'fs';

const memory = fs.readFileSync('input.txt', 'utf8');

const regex = /mul\((\d+),(\d+)\)|do\(\)|don't\(\)/g;
let result = 0;
let enabled = true;
let match: RegExpExecArray | null;

while ((match = regex.exec(memory)) !== null) {
  if (match[0] === 'do()') {
    enabled = true;
  } else if (match[0] === "don't()") {
    enabled = false;
  } else if (enabled) {
    const x = parseInt(match[1], 10);
    const y = parseInt(match[2], 10);
    result += x * y;
  }
}

console.log(result);
