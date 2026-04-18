package main

import "fmt"

var d map[int]int

func Power(a int, b int, c int) int {
	if b == 1 {
		return a % c
	}

	if i, j := d[b]; j {
		return i
	}

	if b%2 == 0 {
		d[b] = (Power(a, b/2, c) * Power(a, b/2, c)) % c
	} else {
		d[b] = (Power(a, b-1, c) * a) % c
	}

	return d[b]
}

func main() {
	var a int
	var b int
	var c int

	d = make(map[int]int)

	_, _ = fmt.Scanf("%d %d %d", &a, &b, &c)

	fmt.Printf("%d", Power(a, b, c))
}
