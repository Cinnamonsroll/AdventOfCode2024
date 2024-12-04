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

	var leftList []int
	var rightList []int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		left, _ := strconv.Atoi(parts[0])
		right, _ := strconv.Atoi(parts[1])
		leftList = append(leftList, left)
		rightList = append(rightList, right)
	}

	sum := 0
	for i := range leftList {
		sum += leftList[i] + rightList[i]
	}

	fmt.Println(sum)
}
