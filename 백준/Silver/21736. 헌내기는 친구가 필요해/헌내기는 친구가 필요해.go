package main

import (
	"bufio"
	"fmt"
	"os"
)

var arr [][]rune
var isVisited [][]bool
var result int = 0
var n int
var m int

func dfs(x, y int) {
	if isVisited[x][y] {
		return
	}

	isVisited[x][y] = true
	if arr[x][y] == 'P' {
		result++
	}

	next := [4][2]int{
		{x + 1, y},
		{x - 1, y},
		{x, y + 1},
		{x, y - 1},
	}

	for _, i := range next {
		if 0 <= i[0] && i[0] < n && 0 <= i[1] && i[1] < m && !isVisited[i[0]][i[1]] && arr[i[0]][i[1]] != 'X' {
			dfs(i[0], i[1])
		}
	}
}

func main() {
	inp := bufio.NewReader(os.Stdin)

	_, _ = fmt.Fscanf(inp, "%d %d\n", &n, &m)

	arr = make([][]rune, n)
	isVisited = make([][]bool, n)
	var startX int
	var startY int

	for i := range n {
		arr[i] = make([]rune, m)
		isVisited[i] = make([]bool, m)
		for j := range m {
			_, _ = fmt.Fscanf(inp, "%c", &arr[i][j])
			if arr[i][j] == 'I' {
				startX = i
				startY = j
			}
			isVisited[i][j] = false
		}
		_, _ = fmt.Fscanf(inp, "\n")
	}

	dfs(startX, startY)

	if result == 0 {
		fmt.Printf("TT\n")
	} else {
		fmt.Printf("%d\n", result)
	}
}
