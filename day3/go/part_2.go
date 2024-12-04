package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	re := regexp.MustCompile(`mul\(\d+,\d+\)|do\(\)|don't\(\)`)
	matches := re.FindAllString(string(content), -1)

	enabled := true
	result := 0

	mulRe := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	for _, instr := range matches {
		switch instr {
		case "do()":
			enabled = true
		case "don't()":
			enabled = false
		default:
			if enabled {
				if mulMatch := mulRe.FindStringSubmatch(instr); mulMatch != nil {
					x, _ := strconv.Atoi(mulMatch[1])
					y, _ := strconv.Atoi(mulMatch[2])
					result += x * y
				}
			}
		}
	}

	fmt.Println(result)
}
