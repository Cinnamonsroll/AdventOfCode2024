import * as fs from 'fs';

const input = fs.readFileSync('input.txt', 'utf-8').trim().split('\n');
let total = 0;

for (const line of input) {
    const [testValue, nums] = line.split(':');
    const numbers = nums.trim().split(/\s+/).map(Number);
    const opsCount = numbers.length - 1;
    let found = false;

    for (let i = 0; i < (1 << (2 * opsCount)) && !found; i++) {
        let result = numbers[0];
        let valid = true;
        for (let j = 0; j < opsCount && valid; j++) {
            const op = (i >> (2 * j)) & 3;
            switch (op) {
                case 0:
                    result += numbers[j + 1];
                    break;
                case 1:
                    result -= numbers[j + 1];
                    break;
                case 2:
                    result *= numbers[j + 1];
                    break;
                case 3:
                    if (numbers[j + 1] === 0 || result % numbers[j + 1] !== 0) {
                        valid = false;
                    } else {
                        result /= numbers[j + 1];
                    }
                    break;
            }
        }
        if (valid && result === Number(testValue)) {
            total += Number(testValue);
            found = true;
        }
    }
}

console.log(total);
