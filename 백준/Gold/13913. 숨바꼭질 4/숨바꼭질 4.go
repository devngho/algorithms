package main

import (
	"bufio"
	"fmt"
	"os"
)

type Route__ struct {
	t    int
	pos  int
	prev *Route__
}

func main() {
	writer := bufio.NewWriter(os.Stdout)
	defer func(writer *bufio.Writer) {
		_ = writer.Flush()
	}(writer)

	var n int
	var k int

	_, _ = fmt.Scanf("%d %d", &n, &k)

	if n == k {
		_, _ = fmt.Fprintf(writer, "0\n%d\n", n)
		return
	}

	pos := make([]Route__, 0)
	pos = append(pos, Route__{0, n, nil})
	visited := make([]int, 100001)

	for {
		i := pos[0]
		pos = pos[1:]

		cur := i.pos

		n := cur + 1
		if 0 <= n && n <= 100000 && visited[n] == 0 {
			if n == k {
				_, _ = fmt.Fprintf(writer, "%d\n", i.t+1)
				res := make([]int, 0)
				for r := &i; r != nil; r = r.prev {
					res = append(res, r.pos)
				}
				for j := len(res) - 1; j >= 0; j-- {
					_, _ = fmt.Fprintf(writer, "%d ", res[j])
				}
				_, _ = fmt.Fprintf(writer, "%d\n", n)
				break
			}
			pos = append(pos, Route__{i.t + 1, n, &i})
			visited[n] = 1
		}

		n = cur - 1
		if 0 <= n && n <= 100000 && visited[n] == 0 {
			if n == k {
				_, _ = fmt.Fprintf(writer, "%d\n", i.t+1)
				res := make([]int, 0)
				for r := &i; r != nil; r = r.prev {
					res = append(res, r.pos)
				}
				for j := len(res) - 1; j >= 0; j-- {
					_, _ = fmt.Fprintf(writer, "%d ", res[j])
				}
				_, _ = fmt.Fprintf(writer, "%d\n", n)
				break
			}
			pos = append(pos, Route__{i.t + 1, n, &i})
			visited[n] = 1
		}

		n = cur * 2
		if 0 <= n && n <= 100000 && visited[n] == 0 {
			if n == k {
				_, _ = fmt.Fprintf(writer, "%d\n", i.t+1)
				res := make([]int, 0)
				for r := &i; r != nil; r = r.prev {
					res = append(res, r.pos)
				}
				for j := len(res) - 1; j >= 0; j-- {
					_, _ = fmt.Fprintf(writer, "%d ", res[j])
				}
				_, _ = fmt.Fprintf(writer, "%d\n", n)
				break
			}
			pos = append(pos, Route__{i.t + 1, n, &i})
			visited[n] = 1
		}
	}
}
