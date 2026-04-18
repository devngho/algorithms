package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Total(arr []int, h int) int {
	total := 0

	for i := range arr {
		total += max(0, arr[i]-h)
	}

	return total
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer func(writer *bufio.Writer) {
		_ = writer.Flush()
	}(writer)

	var n int
	var m int

	_, _ = fmt.Fscanf(reader, "%d %d\n", &n, &m)

	trees := make([]int, n)
	maxTree := 0

	line, _ := reader.ReadString('\n')
	for idx, v := range strings.Split(line[:len(line)-1], " ") {
		n, _ := strconv.Atoi(v)
		trees[idx] = n

		if maxTree < n {
			maxTree = n
		}
	}

	left, right, mid := 0, maxTree, (maxTree)/2

	for {
		total := Total(trees, mid)

		if left == mid {
			break
		}

		if total < m {
			right, mid = mid, (left+mid)/2
		} else if total == m {
			break
		} else {
			left, mid = mid, (right+mid)/2
		}
	}

	fmt.Printf("%d", mid)
}
