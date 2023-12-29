//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/18.
//

import Foundation

struct Deque {
	var input = [Int]()
	var output = [Int]()
	
	var count: Int {
		return input.count + output.count
	}
	
	func index(of item: Int) -> Int {
		let queue = output.reversed() + input
		return queue.firstIndex(of: item)!
	}
	
	mutating func pushRight(_ item: Int) {
		input.append(item)
	}
	
	mutating func pushLeft(_ item: Int) {
		output.append(item)
	}
	
	mutating func popLeft() -> Int {
		if output.isEmpty {
			output = input.reversed()
			input.removeAll()
		}
		return output.popLast()!
	}
	
	mutating func popRight() -> Int {
		if input.isEmpty {
			input = output.reversed()
			output.removeAll()
		}
		return input.popLast()!
	}
}
