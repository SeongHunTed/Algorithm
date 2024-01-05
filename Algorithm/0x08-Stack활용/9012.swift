//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/5/24.
//

import Foundation

func isVPS(_ string: String) -> Bool {
	var stack = [Character]()
	
	for char in string {
		if char == "(" {
			stack.append(char)
			continue
		}
		
		if char == ")" {
			if stack.isEmpty {
				return false
			}
			
			stack.removeLast()
		}
	}
	
	if stack.isEmpty {
		return true
	}
	
	return false
}

let n = Int(readLine()!)!

for _ in 0..<n {
	let ps = readLine()!
	if isVPS(ps) {
		print("YES")
	} else {
		print("NO")
	}
}
