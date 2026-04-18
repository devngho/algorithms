package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
)

func main() {
	inp := bufio.NewReader(os.Stdin)

	var n int

	_, _ = fmt.Fscanf(inp, "%d\n", &n)

	if n == 0 {
		fmt.Printf("0")
		return
	}

	opinions := make([]int, n)
	for i := 0; i < n; i++ {
		_, _ = fmt.Fscanf(inp, "%d\n", &opinions[i])
	}

	slices.Sort(opinions)

	cutoff := int(math.Round(float64(n) * 0.15))

	opinionsCutoff := opinions[cutoff : n-cutoff]
	sum := 0

	for _, v := range opinionsCutoff {
		sum += v
	}

	avg := int(math.Round(float64(sum) / float64(len(opinionsCutoff))))

	fmt.Printf("%d", avg)
}
