//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/5/24.
//

import Foundation

func isGoodWord(_ word: String) -> Bool {
	var stack = [Character]()
	
	for char in word {
		if stack.isEmpty {
			stack.append(char)
			continue
		}
		
		if stack.last! == char {
			stack.removeLast()
			continue
		}
		
		stack.append(char)
	}
	
	if stack.isEmpty {
		return true
	}
	return false
}

let n = Int(readLine()!)!
var counter = 0

for _ in 0..<n {
	let word = readLine()!
	if isGoodWord(word) {
		counter += 1
	}
}

print(counter)
