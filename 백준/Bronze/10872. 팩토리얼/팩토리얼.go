package main

import "fmt"

func main() {
	x := 1
	var n int

	_, _ = fmt.Scanf("%d", &n)

	for i := 1; i <= n; i++ {
		x *= i
	}

	fmt.Printf("%d", x)
}
