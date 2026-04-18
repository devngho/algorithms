package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer func(writer *bufio.Writer) {
		_ = writer.Flush()
	}(writer)

	var n int
	var m int

	_, _ = fmt.Fscanf(reader, "%d %d\n", &n, &m)

	matrix := make([][]int, n)
	for i := 0; i < n; i++ {
		matrix[i] = make([]int, m)
		
		line, _ := reader.ReadString('\n')

		s := strings.Split(line[:len(line)-1], " ")
		for j, v := range s {
			matrix[i][j], _ = strconv.Atoi(v)
		}
	}

	for i := 0; i < n; i++ {
		line, _ := reader.ReadString('\n')

		s := strings.Split(line[:len(line)-1], " ")
		for j, v := range s {
			r, _ := strconv.Atoi(v)

			matrix[i][j] += r
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			_, _ = fmt.Fprintf(writer, "%d ", matrix[i][j])
		}
		_, _ = fmt.Fprintln(writer)
	}
}
