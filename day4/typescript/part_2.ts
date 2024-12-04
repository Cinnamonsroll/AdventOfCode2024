import * as fs from "fs";

function countXmasXShape(grid: string[][]): number {
  let count = 0;
  const rows = grid.length;
  const cols = grid[0].length;

  function checkXmasXShape(x: number, y: number): boolean {
    if (grid[x][y] !== "A") {
      return false;
    }

    const topLeft = grid[x - 1][y - 1] + grid[x + 1][y + 1];
    const topRight = grid[x - 1][y + 1] + grid[x + 1][y - 1];

    return (
      (topLeft === "MS" || topLeft === "SM") &&
      (topRight === "MS" || topRight === "SM")
    );
  }

  for (let x = 1; x < rows - 1; x++) {
    for (let y = 1; y < cols - 1; y++) {
      if (checkXmasXShape(x, y)) {
        count++;
      }
    }
  }

  return count;
}

const gridXShape: string[][] = fs
  .readFileSync("input.txt", "utf-8")
  .split("\n")
  .map((line) => line.split(""));

console.log(countXmasXShape(gridXShape));
