package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	total := 0

	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), ":")
		testValue, _ := strconv.Atoi(parts[0])
		numStrs := strings.Fields(parts[1])
		numbers := make([]int, len(numStrs))
		for i, n := range numStrs {
			numbers[i], _ = strconv.Atoi(n)
		}

		opsCount := len(numbers) - 1
		for i := 0; i < 1<<opsCount; i++ {
			result := numbers[0]
			for j := 0; j < opsCount; j++ {
				if (i>>j)&1 == 0 {
					result += numbers[j+1]
				} else {
					result *= numbers[j+1]
				}
			}
			if result == testValue {
				total += testValue
				break
			}
		}
	}

	fmt.Println(total)
}
