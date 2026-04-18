package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer func(writer *bufio.Writer) {
		_ = writer.Flush()
	}(writer)

	var line string
	_, _ = fmt.Fscanln(reader, &line)

	diff := (uint8)('a' - 'A')

	for i := 0; i < len(line); i++ {
		if 'a' <= line[i] && line[i] <= 'z' {
			_, _ = fmt.Fprintf(writer, "%c", line[i]-diff)
		} else {
			_, _ = fmt.Fprintf(writer, "%c", line[i]+diff)
		}
	}
}
