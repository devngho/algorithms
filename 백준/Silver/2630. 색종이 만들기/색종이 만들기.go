package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func CheckIsAllEqual(arr [][]int) bool {
	color := arr[0][0]
	n := len(arr)

	for x := 0; x < n; x++ {
		for y := 0; y < n; y++ {
			if arr[x][y] != color {
				return false
			}
		}
	}

	return true
}

func Cut(arr [][]int) (int, int) { // white to blue
	if CheckIsAllEqual(arr) {
		if arr[0][0] == 0 {
			return 1, 0
		} else {
			return 0, 1
		}
	}

	n := len(arr)
	half := n / 2
	white, blue := 0, 0

	top_left := make([][]int, half)
	top_right := make([][]int, half)
	bottom_left := make([][]int, half)
	bottom_right := make([][]int, half)

	for x := 0; x < half; x++ {
		top_left[x] = make([]int, half)
		top_right[x] = make([]int, half)
		bottom_left[x] = make([]int, half)
		bottom_right[x] = make([]int, half)
	}

	for x := 0; x < n; x++ {
		for y := 0; y < n; y++ {
			if x >= half {
				if y >= half {
					bottom_right[x-half][y-half] = arr[x][y]
				} else {
					bottom_left[x-half][y] = arr[x][y]
				}
			} else {
				if y >= half {
					top_right[x][y-half] = arr[x][y]
				} else {
					top_left[x][y] = arr[x][y]
				}
			}
		}
	}

	a, b := Cut(top_left)
	white += a
	blue += b
	a, b = Cut(top_right)
	white += a
	blue += b
	a, b = Cut(bottom_left)
	white += a
	blue += b
	a, b = Cut(bottom_right)
	white += a
	blue += b

	return white, blue
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer func(writer *bufio.Writer) {
		_ = writer.Flush()
	}(writer)

	var n int
	var line string

	_, _ = fmt.Fscanln(reader, &n)

	arr := make([][]int, n)
	for x := 0; x < n; x++ {
		arr[x] = make([]int, n)
		line, _ = reader.ReadString('\n')

		s := strings.Split(line[:len(line)-1], " ")
		for idx, i := range s {
			arr[x][idx], _ = strconv.Atoi(i)
		}
	}

	white, blue := Cut(arr)
	_, _ = fmt.Fprintf(writer, "%d\n%d\n", white, blue)
}
