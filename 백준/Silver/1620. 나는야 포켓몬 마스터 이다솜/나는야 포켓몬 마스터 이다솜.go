package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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

	arr := make([]string, n)
	mapping := make(map[string]int)
	for i := 0; i < n; i++ {
		line, _ := reader.ReadString('\n')
		arr[i] = line[:len(line)-1]
		mapping[arr[i]] = i + 1
	}

	for i := 0; i < m; i++ {
		line, _ := reader.ReadString('\n')
		line = line[:len(line)-1]

		if '0' <= line[0] && line[0] <= '9' {
			idx, _ := strconv.Atoi(line)
			_, _ = fmt.Fprintln(writer, arr[idx-1])
		} else {
			_, _ = fmt.Fprintln(writer, mapping[line])
		}
	}
}
