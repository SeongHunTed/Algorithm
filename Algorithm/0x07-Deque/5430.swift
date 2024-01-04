//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/3/24.
//

import Foundation

var result = ""

var testCase = Int(readLine()!)!

while testCase > 0 {
	let function = readLine()!
	let n = Int(readLine()!)!
	let array = readLine()!
		.replacingOccurrences(of: "[\\[\\]]", with: "", options: .regularExpression)
		.split(separator: ",")
		.map { Int(String($0)) }
	
	var front = 0
	var end = n - 1
	var reverse = false
	var error = false
	
	for query in function {
		switch String(query) {
			case "R":
				swap(&front, &end)
				reverse.toggle()
			case "D":
				if !reverse && front <= end {
					front += 1
				} else if reverse && front >= end {
					front -= 1
				} else {
					error = true
					break
				}
			default:
				break
		}
	}
	
	if error {
		result.write("error\n")
	} else {
		result.write("[")
		while (!reverse && front <= end) || (reverse && front >= end) {
			let word = array[front]!
			result.write("\(word)")
			if front != end { result.write(",") }
			front += reverse ? -1 : 1
		}
		result.write("]\n")
	}
	testCase -= 1
}

print(result)
