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
		found := false
		for i := 0; i < 1<<(2*opsCount) && !found; i++ {
			result := numbers[0]
			valid := true
			for j := 0; j < opsCount && valid; j++ {
				op := (i >> (2 * j)) & 3
				switch op {
				case 0:
					result += numbers[j+1]
				case 1:
					result -= numbers[j+1]
				case 2:
					result *= numbers[j+1]
				case 3:
					if numbers[j+1] == 0 || result%numbers[j+1] != 0 {
						valid = false
					} else {
						result /= numbers[j+1]
					}
				}
			}
			if valid && result == testValue {
				total += testValue
				found = true
			}
		}
	}

	fmt.Println(total)
}
