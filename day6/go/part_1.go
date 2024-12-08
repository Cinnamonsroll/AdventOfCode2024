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

	scanner := bufio.NewScanner(file)
	var grid [][]rune

	for scanner.Scan() {
		line := scanner.Text()
		grid = append(grid, []rune(line))
	}

	N := len(grid)
	M := len(grid[0])
	var startX, startY int

	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			if grid[i][j] == '^' {
				startY, startX = i, j
				break
			}
		}
	}

	visited := make(map[string]bool)
	visited[fmt.Sprintf("%d,%d", startY, startX)] = true
	queue := [][]int{{startY, startX}}

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		y, x := curr[0], curr[1]

		for _, dir := range [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
			newY, newX := y+dir[0], x+dir[1]
			if newY >= 0 && newY < N && newX >= 0 && newX < M && grid[newY][newX] != '#' {
				key := fmt.Sprintf("%d,%d", newY, newX)
				if !visited[key] {
					visited[key] = true
					queue = append(queue, []int{newY, newX})
				}
			}
		}
	}

	fmt.Println(len(visited))
}
