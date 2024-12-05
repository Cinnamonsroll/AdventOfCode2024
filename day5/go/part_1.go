package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Rule [2]int
type Update []int

func parseInput(filePath string) ([]Rule, []Update) {
	file, err := os.Open(filePath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var rules []Rule
	var updates []Update
	section := 0

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line == "" {
			section++
			continue
		}

		if section == 0 {
			parts := strings.Split(line, "|")
			a, _ := strconv.Atoi(parts[0])
			b, _ := strconv.Atoi(parts[1])
			rules = append(rules, Rule{a, b})
		} else {
			var update Update
			for _, numStr := range strings.Split(line, ",") {
				num, _ := strconv.Atoi(numStr)
				update = append(update, num)
			}
			updates = append(updates, update)
		}
	}

	return rules, updates
}

func isUpdateOrdered(update Update, rules []Rule) bool {
	pageIndices := make(map[int]int)
	for i, page := range update {
		pageIndices[page] = i
	}

	for _, rule := range rules {
		if i1, ok1 := pageIndices[rule[0]]; ok1 {
			if i2, ok2 := pageIndices[rule[1]]; ok2 {
				if i1 > i2 {
					return false
				}
			}
		}
	}
	return true
}

func main() {
	rules, updates := parseInput("input.txt")
	middleSum := 0

	for _, update := range updates {
		if isUpdateOrdered(update, rules) {
			middleSum += update[len(update)/2]
		}
	}

	fmt.Println(middleSum)
}
