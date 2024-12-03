const fs = require("fs");

const memory = fs.readFileSync("input.txt", "utf8");

const isDigit = (c) => c >= "0" && c <= "9";
let result = 0;
let i = 0;

function parseNumber(i) {
  let num = 0;
  while (i < memory.length && isDigit(memory[i])) {
    num = num * 10 + (memory[i].charCodeAt(0) - '0'.charCodeAt(0));
    i++;
  }
  return { num, i };
}

while (i < memory.length) {
  if (memory.slice(i, i + 3) === "mul") {
    i += 3;
    if (memory[i] === "(") {
      i++;
      const { num: num1, i: newI1 } = parseNumber(i);
      i = newI1;
      if (memory[i] === ",") {
        i++;
        const { num: num2, i: newI2 } = parseNumber(i);
        i = newI2;
        if (memory[i] === ")") {
          i++;
          result += num1 * num2;
        }
      }
    }
  } else {
    i++;
  }
}

console.log(result);
