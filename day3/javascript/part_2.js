const fs = require("fs");

const memory = fs.readFileSync("input.txt", "utf8");

const isDigit = (c) => c >= "0" && c <= "9";
let result = 0;
let enabled = true;

function parseNumber(i) {
  let num = 0;
  while (i < memory.length && isDigit(memory[i])) {
    num = num * 10 + (memory[i].charCodeAt(0) - '0'.charCodeAt(0));
    i++;
  }
  return { num, i };
}

for (let i = 0; i < memory.length;) {
  if (memory.slice(i, i + 3) === "mul") {
    i += 3;
    if (memory[i] === '(') {
      i++;
      const { num: num1, i: newI1 } = parseNumber(i);
      i = newI1;
      if (memory[i] === ',') {
        i++;
        const { num: num2, i: newI2 } = parseNumber(i);
        i = newI2;
        if (memory[i] === ')') {
          i++;
          if (enabled) {
            result += num1 * num2;
          }
        }
      }
    }
  } else if (memory.slice(i, i + 4) === "do()") {
    enabled = true;
    i += 4;
  } else if (memory.slice(i, i + 7) === "don't()") {
    enabled = false;
    i += 7;
  } else {
    i++;
  }
}

console.log(result);
