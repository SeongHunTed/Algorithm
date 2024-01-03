//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 12/29/23.
//

import Foundation

extension Deque {
	mutating func moveLeft() {
		pushRight(popLeft())
	}
	
	mutating func moveRight() {
		pushLeft(popRight())
	}
}

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0]
let m = input[1]

let position = readLine()!.split(separator: " ").map { Int($0)! }
var counter = 0

var deque = Deque()
for i in 1...n {
	deque.pushRight(i)
}

position.forEach { item in
	let moveLeftCounter = deque.index(of: item)
	let moveRightCounter = deque.count - moveLeftCounter
	
	if moveLeftCounter < moveRightCounter {
		for _ in 0..<moveLeftCounter {
			deque.moveLeft()
		}
		_ = deque.popLeft()
		counter += moveLeftCounter
	} else {
		for _ in 0..<moveRightCounter {
			deque.moveRight()
		}
		_ = deque.popLeft()
		counter += moveRightCounter
	}
}

print(counter)
