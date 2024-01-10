//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/18.
//

import Foundation

struct Deque<T> {
	var input = [T]()
	var output = [T]()
	
	var count: Int {
		return input.count + output.count
	}
	
	var isEmpty: Bool {
		return input.isEmpty && output.isEmpty
	}
	
	mutating func pushRight(_ item: T) {
		input.append(item)
	}
	
	mutating func pushLeft(_ item: T) {
		output.append(item)
	}
	
	mutating func popLeft() -> T {
		if output.isEmpty {
			output = input.reversed()
			input.removeAll()
		}
		return output.popLast()!
	}
	
	mutating func popRight() -> T {
		if input.isEmpty {
			input = output.reversed()
			output.removeAll()
		}
		return input.popLast()!
	}
}
