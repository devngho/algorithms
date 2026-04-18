package main

func sum(a []int) int {
	result := 0
	for _, i := range a {
		result += i
	}
	return result
}
