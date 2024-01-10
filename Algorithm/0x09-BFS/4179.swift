//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/10/24.
//

import Foundation

enum Structure: String {
	case wall = "#"
	case way = "."
	case first = "J"
	case fire = "F"
}

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let r = input[0]
let c = input[1]

let dx = [1, 0, -1, 0]
let dy = [0, 1, 0, -1]

var time = 0
var success = false
var map = Array(repeating: [""], count: r)
var check = Array(repeating: Array(repeating: false, count: c), count: r)
var queue = Deque<(Int, Int)>()
var fireQueue = Deque<(Int, Int)>()

for i in 0..<r {
	let line = readLine()!.map { String($0) }
	map[i] = line
	for j in 0..<c{
		if map[i][j] == Structure.first.rawValue {
			map[i][j] = "."
			check[i][j] = true
			queue.pushRight((i, j))
		} else if map[i][j] == Structure.fire.rawValue {
			fireQueue.pushRight((i, j))
		}
	}
}

func spreadFire() {
	for _ in 0..<fireQueue.count {
		let position = fireQueue.popLeft()
		
		for i in 0..<4 {
			let nx = position.0 + dx[i]
			let ny = position.1 + dy[i]
			
			if nx >= 0 && ny >= 0 && nx < r && ny < c && map[nx][ny] == "." {
				map[nx][ny] = "F"
				fireQueue.pushRight((nx, ny))
			}
		}
	}
}

func escape() {
	for _ in 0..<queue.count {
		let position = queue.popLeft()
		for i in 0..<4 {
			let nx = position.0 + dx[i]
			let ny = position.1 + dy[i]
			
			if nx >= 0 && ny >= 0 && nx < r && ny < c {
				if map[nx][ny] == "." {
					map[nx][ny] = "J"
					queue.pushRight((nx, ny))
				}
			} else {
				success = true
				break
			}
		}
	}
}

while !success && !queue.isEmpty {
	time += 1
	spreadFire()
	escape()
//	for row in map {
//		print(row)
//	}
//	print(queue)
//	print(success)
}
if success {
	print(time)
} else {
	print("IMPOSSIBLE")
}

