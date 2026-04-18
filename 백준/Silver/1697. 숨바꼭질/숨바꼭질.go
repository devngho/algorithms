package main

import "fmt"

type Route struct {
	t   int
	pos int
}

func main() {
	var n int
	var k int

	_, _ = fmt.Scanf("%d %d", &n, &k)

	if n == k {
		fmt.Printf("0")
		return
	}

	pos := make([]Route, 0)
	pos = append(pos, Route{0, n})
	visited := make([]int, 100001)

	for {
		i := pos[0]
		pos = pos[1:]

		n := i.pos + 1
		if 0 <= n && n <= 100000 && visited[n] == 0 {
			if n == k {
				fmt.Printf("%d", i.t+1)
				break
			}
			pos = append(pos, Route{i.t + 1, n})
			visited[n] = 1
		}

		n = i.pos - 1
		if 0 <= n && n <= 100000 && visited[n] == 0 {
			if n == k {
				fmt.Printf("%d", i.t+1)
				break
			}
			pos = append(pos, Route{i.t + 1, n})
			visited[n] = 1
		}

		n = i.pos * 2
		if 0 <= n && n <= 100000 && visited[n] == 0 {
			if n == k {
				fmt.Printf("%d", i.t+1)
				break
			}
			pos = append(pos, Route{i.t + 1, n})
			visited[n] = 1
		}
	}
}
