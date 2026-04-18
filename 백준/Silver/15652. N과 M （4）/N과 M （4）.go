package main

import (
	"bufio"
	"fmt"
	"os"
)

func Permutation2(start int, max int, count int) [][]int {
	if count == 0 {
		return [][]int{{}}
	}

	list := make([][]int, 0)

	for a := start; a <= max; a++ {
		n := make([]int, 0)
		n = append(n, a)

		for _, b := range Permutation2(a, max, count-1) {
			m := make([]int, len(n))
			copy(m, n)
			m = append(m, b...)

			list = append(list, m)
		}
	}

	return list
}

func main() {
	writer := bufio.NewWriter(os.Stdout)
	defer func(writer *bufio.Writer) {
		_ = writer.Flush()
	}(writer)

	var n int
	var m int

	_, _ = fmt.Scanf("%d %d", &n, &m)

	list := Permutation2(1, n, m)

	for _, i := range list {
		for _, j := range i {
			_, _ = fmt.Fprintf(writer, "%d ", j)
		}
		_, _ = fmt.Fprintf(writer, "\n")
	}
}
