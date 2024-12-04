package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isSafeReport(report []int) bool {
	differences := make([]int, len(report)-1)
	for i := 1; i < len(report); i++ {
		differences[i-1] = report[i] - report[i-1]
	}

	allIncreasing := true
	allDecreasing := true

	for _, diff := range differences {
		if diff < 1 || diff > 3 {
			allIncreasing = false
		}
		if diff < -3 || diff > -1 {
			allDecreasing = false
		}
	}

	return allIncreasing || allDecreasing
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	safeCount := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var report []int
		for _, numStr := range strings.Fields(scanner.Text()) {
			num, _ := strconv.Atoi(numStr)
			report = append(report, num)
		}
		if isSafeReport(report) {
			safeCount++
		}
	}

	fmt.Println(safeCount)
}
