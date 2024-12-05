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

func sortUpdate(update Update, rules []Rule) Update {
	dependencies := make(map[int]map[int]bool)
	for _, page := range update {
		dependencies[page] = make(map[int]bool)
	}

	for _, rule := range rules {
		if _, ok1 := dependencies[rule[0]]; ok1 {
			if _, ok2 := dependencies[rule[1]]; ok2 {
				dependencies[rule[1]][rule[0]] = true
			}
		}
	}

	visited := make(map[int]bool)
	var sortedUpdate Update

	var dfs func(int)
	dfs = func(page int) {
		if visited[page] {
			return
		}
		visited[page] = true
		for dep := range dependencies[page] {
			dfs(dep)
		}
		sortedUpdate = append(sortedUpdate, page)
	}

	for _, page := range update {
		dfs(page)
	}

	return sortedUpdate
}

func main() {
	rules, updates := parseInput("input.txt")
	total := 0

	for _, update := range updates {
		sortedUpdate := sortUpdate(update, rules)
		total += sortedUpdate[len(sortedUpdate)/2]
	}

	fmt.Println(total)
}
