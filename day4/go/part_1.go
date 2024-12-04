package main

import (
	"bufio"
	"fmt"
	"os"
)

func countXmas(grid [][]rune) int {
	word := "XMAS"
	directions := [][2]int{
		{-1, 0}, {1, 0}, {0, -1}, {0, 1},
		{-1, -1}, {-1, 1}, {1, -1}, {1, 1},
	}
	count := 0

	valid := func(r, c, dr, dc int) bool {
		for i, ch := range word {
			nr, nc := r+dr*i, c+dc*i
			if nr < 0 || nr >= len(grid) || nc < 0 || nc >= len(grid[0]) {
				return false
			}
			if grid[nr][nc] != ch {
				return false
			}
		}
		return true
	}

	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[0]); c++ {
			for _, dir := range directions {
				if valid(r, c, dir[0], dir[1]) {
					count++
				}
			}
		}
	}

	return count
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var grid [][]rune
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		grid = append(grid, []rune(scanner.Text()))
	}

	fmt.Println(countXmas(grid))
}
