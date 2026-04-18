package main

import "fmt"

func main() {
	var line string
	_, _ = fmt.Scanln(&line)
	fmt.Printf("%d", len(line))
}
