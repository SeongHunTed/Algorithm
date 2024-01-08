//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/5/24.
//

import Foundation

func splitWithLazer(structure: [Character]) -> Int {
	var stack = [Character]()
	var totalPipe = 0
	
	for i in 0..<structure.count {
		if structure[i] == "(" {
			stack.append("(")
			continue
		}
		
		if structure[i] == ")" && structure[i-1] == "(" {
			stack.removeLast()
			totalPipe += stack.count
		} else {
			stack.removeLast()
			totalPipe += 1
		}
	}
	return totalPipe
}

let structrue = Array(readLine()!)
let total = splitWithLazer(structure: structrue)
print(total)
