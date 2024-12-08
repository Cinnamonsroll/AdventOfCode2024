package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var grid []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			continue
		}
		grid = append(grid, line)
	}

	N, M := len(grid), len(grid[0])
	nodes := make(map[rune][]struct{ x, y int })

	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			if grid[i][j] != '.' {
				nodes[rune(grid[i][j])] = append(nodes[rune(grid[i][j])], struct{ x, y int }{j, i})
			}
		}
	}

	antinodes := make(map[struct{ x, y int }]bool)

	for _, nodeList := range nodes {
		L := len(nodeList)
		for i := 0; i < L; i++ {
			for j := 0; j < i; j++ {
				node1, node2 := nodeList[i], nodeList[j]
				x1, y1 := node1.x, node1.y
				x2, y2 := node2.x, node2.y
				newX, newY := x2+(x2-x1), y2+(y2-y1)
				if newX >= 0 && newX < M && newY >= 0 && newY < N {
					antinodes[struct{ x, y int }{newX, newY}] = true
				}
				x1, y1 = node2.x, node2.y
				x2, y2 = node1.x, node1.y
				newX, newY = x2+(x2-x1), y2+(y2-y1)
				if newX >= 0 && newX < M && newY >= 0 && newY < N {
					antinodes[struct{ x, y int }{newX, newY}] = true
				}
			}
		}
	}

	fmt.Println(len(antinodes))
}
