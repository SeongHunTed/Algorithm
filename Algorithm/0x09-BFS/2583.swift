//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/12/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

let r = input[0]
let c = input[1]
let count = input[2]

var paper = Array(repeating: Array(repeating: 0, count: c), count: r)
var visit = Array(repeating: Array(repeating: false, count: c), count: r)
var area = 0

for _ in 0..<count {
	let line = readLine()!.split(separator: " ").map { Int(String($0))! }
	let start = (line[1], line[0])
	let end = (line[3], line[2])
	
	for i in start.0..<end.0 {
		for j in start.1..<end.1 {
			paper[i][j] = -1
		}
	}
}

//for row in paper {
//	print(row)
//}
//print()

func explore(_ i: Int, _ j: Int ) -> Int {
	var dimension = 0
	var queue = [(i, j)]
	visit[i][j] = true
	paper[i][j] = 8
	var index = 0
	let dx = [1, 0, -1 ,0]
	let dy = [0, 1, 0, -1]
	
	while index < queue.count {
		let position = queue[index]
		
		for k in 0..<4 {
			let nx = position.0 + dx[k]
			let ny = position.1 + dy[k]
			
			if nx >= 0 && ny >= 0 && nx < r && ny < c && !visit[nx][ny] && paper[nx][ny] != -1 {
				visit[nx][ny] = true
				paper[nx][ny] = 8
				queue.append((nx, ny))
			}
		}
		index += 1
		dimension += 1
	}
	
	return dimension
}

var dimensions = [Int]()

for i in 0..<r {
	for j in 0..<c {
		if paper[i][j] == 0 {
			dimensions.append(explore(i, j))
			area += 1
		}
	}
}

print(dimensions.count)
print(dimensions.sorted().map { String($0) }.joined(separator: " "))
