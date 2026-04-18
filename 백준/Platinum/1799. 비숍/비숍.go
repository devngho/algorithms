package main

import (
	"fmt"
	"maps"
)

func backtrack(n int, pos [][]int, cur int, diagonals map[int]struct{}) int {
	if cur >= len(pos) {
		return 0
	}

	incId := pos[cur][0] + pos[cur][1]
	decId := -(n + pos[cur][1] - pos[cur][0])

	_, ok1 := diagonals[incId]
	_, ok2 := diagonals[decId]

	res := 0

	if !ok1 && !ok2 {
		newMap := maps.Clone(diagonals)
		newMap[incId] = struct{}{}
		newMap[decId] = struct{}{}

		res = backtrack(n, pos, cur+1, newMap) + 1
	}

	return max(
		backtrack(n, pos, cur+1, diagonals),
		res,
	)
}

func main() {
	var n int

	fmt.Scanf("%d\n", &n)

	odd_pos := make([][]int, 0)
	even_pos := make([][]int, 0)
	tmp := 0

	for j := range n {
		for i := range n {
			fmt.Scanf("%d", &tmp)

			if tmp == 1 {
				if (i+j)%2 == 0 {
					even_pos = append(even_pos, []int{i, j})
				} else {
					odd_pos = append(odd_pos, []int{i, j})
				}
			}
		}
		// fmt.Scanf("\n")
	}

	fmt.Println(backtrack(n, odd_pos, 0, make(map[int]struct{})) + backtrack(n, even_pos, 0, make(map[int]struct{})))
}
