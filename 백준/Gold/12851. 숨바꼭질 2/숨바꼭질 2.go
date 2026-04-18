package main

import "fmt"

type Route_ struct {
	t   int
	pos int
}

func main() {
	var n int
	var k int

	_, _ = fmt.Scanf("%d %d", &n, &k)

	if n == k {
		fmt.Printf("0\n1")
		return
	}

	pos := make([]Route_, 0)
	pos = append(pos, Route_{0, n})
	visited := make([]int, 100001)
	cnt := 0
	res := 0

	for len(pos) > 0 {
		i := pos[0]
		pos = pos[1:]

		if cnt > 0 && res < i.t {
			continue
		}

		if i.pos == k {
			res = i.t
			cnt++
		}

		n := i.pos + 1
		if 0 <= n && n <= 100000 && (visited[n] == 0 || visited[n] == i.t) {
			pos = append(pos, Route_{i.t + 1, n})
			visited[n] = i.t
		}

		n = i.pos - 1
		if 0 <= n && n <= 100000 && (visited[n] == 0 || visited[n] == i.t) {
			pos = append(pos, Route_{i.t + 1, n})
			visited[n] = i.t
		}

		n = i.pos * 2
		if 0 <= n && n <= 100000 && (visited[n] == 0 || visited[n] == i.t) {
			pos = append(pos, Route_{i.t + 1, n})
			visited[n] = i.t
		}
	}

	fmt.Printf("%d\n%d", res, cnt)
}
