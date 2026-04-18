package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Pos struct {
	x int
	y int
	d int
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer func(writer *bufio.Writer) {
		_ = writer.Flush()
	}(writer)

	var n int
	var m int
	var line string

	_, _ = fmt.Fscanln(reader, &n, &m)

	arr := make([][]int, n)
	distance := make([][]int, n)
	cursor := make([]Pos, 0)
	for x := 0; x < n; x++ {
		arr[x] = make([]int, m)
		distance[x] = make([]int, m)
		line, _ = reader.ReadString('\n')

		s := strings.Split(line[:len(line)-1], " ")
		for idx, i := range s {
			arr[x][idx], _ = strconv.Atoi(i)
			distance[x][idx] = -1

			if arr[x][idx] == 2 {
				cursor = append(cursor, Pos{x, idx, 0})
				distance[x][idx] = 0
			} else if arr[x][idx] == 0 {
				distance[x][idx] = 0
			}
		}
	}

	for len(cursor) != 0 {
		current := cursor[0]
		cursor = cursor[1:]

		distance[current.x][current.y] = current.d

		next := Pos{current.x + 1, current.y, current.d + 1}
		if 0 <= next.x && next.x < n && 0 <= next.y && next.y < m && distance[next.x][next.y] == -1 {
			cursor = append(cursor, next)
			distance[next.x][next.y] = -2
		}

		next = Pos{current.x, current.y + 1, current.d + 1}
		if 0 <= next.x && next.x < n && 0 <= next.y && next.y < m && distance[next.x][next.y] == -1 {
			cursor = append(cursor, next)
			distance[next.x][next.y] = -2
		}

		next = Pos{current.x, current.y - 1, current.d + 1}
		if 0 <= next.x && next.x < n && 0 <= next.y && next.y < m && distance[next.x][next.y] == -1 {
			cursor = append(cursor, next)
			distance[next.x][next.y] = -2
		}

		next = Pos{current.x - 1, current.y, current.d + 1}
		if 0 <= next.x && next.x < n && 0 <= next.y && next.y < m && distance[next.x][next.y] == -1 {
			cursor = append(cursor, next)
			distance[next.x][next.y] = -2
		}
	}

	for x := 0; x < n; x++ {
		for y := 0; y < m; y++ {
			_, _ = fmt.Fprintf(writer, "%d ", distance[x][y])
		}
		_, _ = fmt.Fprintf(writer, "\n")
	}
}
