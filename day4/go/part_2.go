package main

import (
	"bufio"
	"fmt"
	"os"
)

func countXmas(grid [][]rune) int {
	ret := 0

	checkXmasXShape := func(x, y int) bool {
		if grid[x][y] != 'A' {
			return false
		}

		topLeft := string([]rune{grid[x-1][y-1], grid[x+1][y+1]})
		topRight := string([]rune{grid[x-1][y+1], grid[x+1][y-1]})

		return (topLeft == "MS" || topLeft == "SM") &&
			(topRight == "MS" || topRight == "SM")
	}

	for x := 1; x < len(grid)-1; x++ {
		for y := 1; y < len(grid[0])-1; y++ {
			if checkXmasXShape(x, y) {
				ret++
			}
		}
	}

	return ret
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
