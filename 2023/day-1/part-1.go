package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"unicode"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		if err = file.Close(); err != nil {
			log.Fatal(err)
		}
	}()

	scanner := bufio.NewScanner(file)

	var total int
	for scanner.Scan() {
		var line string
		line = scanner.Text()
		dig := get_first_and_last_digits(line)
		i := (10 * dig[0]) + dig[1]
		total += i
	}
	fmt.Printf("Total: %v\n", total)
}

func get_first_and_last_digits(line string) [2]int {
	var dig = [2]int{}
	for _, r := range line {
		if unicode.IsDigit(r) {
			i, err := strconv.Atoi(string(r))
			if err != nil {
				log.Fatal(err)
			}
			if dig[0] == 0 {
				dig[0] = i
			}
			dig[1] = i
		}
	}
	return dig
}
