//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/9/24.
//

import Foundation

func parenthesisCount(parenthesises: [String]) -> Int {
	var stack = [String]()
	var value = 1
	var result = 0
	var isValid = true
	
	for i in parenthesises.indices {
		if parenthesises[i] == "(" {
			value *= 2
			stack.append(parenthesises[i])
		} else if parenthesises[i] == "[" {
			value *= 3
			stack.append(parenthesises[i])
		} else if parenthesises[i] == ")" {
			if stack.isEmpty || stack.last != "(" {
				isValid.toggle()
				break
			}
			
			if parenthesises[i-1] == "(" {
				result += value
			}
			stack.removeLast()
			value /= 2
		} else if parenthesises[i] == "]" {
			if stack.isEmpty || stack.last != "[" {
				isValid.toggle()
				break
			}
			
			if parenthesises[i-1] == "[" {
				result += value
			}
			stack.removeLast()
			value /= 3
		}
	}
	
	if !isValid || !stack.isEmpty {
		return 0
	} else {
		return result
	}
}

let parenthesises = readLine()!.map { String($0) }
print(parenthesisCount(parenthesises: parenthesises))
