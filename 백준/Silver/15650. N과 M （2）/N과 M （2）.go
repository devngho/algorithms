package main

import "fmt"

func Permutation(start int, max int, count int) [][]int {
	if count == 0 {
		return [][]int{{}}
	}

	list := make([][]int, 0)

	for a := start; a <= max-count+1; a++ {
		n := make([]int, 0)
		n = append(n, a)

		for _, b := range Permutation(a+1, max, count-1) {
			m := make([]int, len(n))
			copy(m, n)
			m = append(m, b...)

			list = append(list, m)
		}
	}

	return list
}

func main() {
	var n int
	var m int

	_, _ = fmt.Scanf("%d %d", &n, &m)

	list := Permutation(1, n, m)

	for _, i := range list {
		for _, j := range i {
			fmt.Printf("%d ", j)
		}
		fmt.Printf("\n")
	}
}
