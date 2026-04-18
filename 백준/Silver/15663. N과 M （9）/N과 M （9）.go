package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func Permutation3(left []int, max int, count int) [][]int {
	if count == 0 {
		return [][]int{{}}
	}

	list := make([][]int, 0)

	for a := 0; a <= max; a++ {
		if slices.Contains(left, a) {
			continue
		}

		newleft := make([]int, len(left))
		copy(newleft, left)
		newleft = append(newleft, a)

		for _, b := range Permutation3(newleft, max, count-1) {
			m := make([]int, 0)
			m = append(m, a)
			m = append(m, b...)

			list = append(list, m)
		}
	}

	return list
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

	mapping := make([]int, n)
	line, _ := reader.ReadString('\n')

	s := strings.Split(line[:len(line)-1], " ")
	for idx, i := range s {
		mapping[idx], _ = strconv.Atoi(i)
	}

	slices.Sort(mapping)

	list := Permutation3([]int{}, n-1, m)

	//for _, i := range list {
	//	for _, j := range i {
	//		_, _ = fmt.Fprintf(writer, "%d ", j)
	//	}
	//	_, _ = fmt.Fprintf(writer, "\n")
	//}
    
    printed := make(map[string]bool)

	for _, i := range list {
        s := new(strings.Builder)
		for _, j := range i {
			_, _ = fmt.Fprintf(s, "%d ", mapping[j])
		}
        str := s.String()
        if exists := printed[str]; !exists {
            printed[str] = true
		    _, _ = fmt.Fprintf(writer, "%s\n", str)
        }
	}
}
