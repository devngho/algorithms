package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
)

type Document struct {
	priority int
	marked   bool
}

func main() {
	inp := bufio.NewReader(os.Stdin)

	var testcases int

	_, _ = fmt.Fscanf(inp, "%d\n", &testcases)

	for i := 0; i < testcases; i++ {
		var n int
		var m int
		_, _ = fmt.Fscanf(inp, "%d %d\n", &n, &m)

		priorityCounts := make(map[int]int)
		maxPriority := 1
		queue := list.New()

		for j := 0; j < n; j++ {
			var priority int

			_, _ = fmt.Fscanf(inp, "%d ", &priority)

			if _, exists := priorityCounts[priority]; exists {
				priorityCounts[priority]++
			} else {
				priorityCounts[priority] = 1
			}

			if maxPriority < priority {
				maxPriority = priority
			}

			queue.PushBack(Document{priority, j == m})
		}

		//_, _ = fmt.Fscanf(inp, "\n")

		idx := 0
		for {
			v := queue.Front()
			if v == nil {
				break
			}
			queue.Remove(v)
			doc := v.Value.(Document)

			if maxPriority != doc.priority {
				// add to back
				queue.PushBack(doc)
				continue
			}

			idx++

			if doc.marked {
				fmt.Printf("%d\n", idx)
				break
			}

			// adjust counts
			priorityCounts[doc.priority]--
			if priorityCounts[doc.priority] == 0 {
				for priorityCounts[maxPriority] == 0 {
					maxPriority--
				}
			}
		}
	}
}
