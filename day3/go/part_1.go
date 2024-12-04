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

	re := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	matches := re.FindAllStringSubmatch(string(content), -1)

	sum := 0
	for _, match := range matches {
		x, _ := strconv.Atoi(match[1])
		y, _ := strconv.Atoi(match[2])
		sum += x * y
	}

	fmt.Println(sum)
}
