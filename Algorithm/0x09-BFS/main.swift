//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/20/24.
//

import Foundation
//
//let testCase = """
//5 7
//0 0 0 0 0 0 0
//0 2 4 5 3 0 0
//0 3 0 2 5 2 0
//0 7 6 2 4 0 0
//0 0 0 0 0 0 0
//""".split(separator: "\n")
//
//let r = 5
//let c = 7

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
//
let r = input[0]
let c = input[1]

var map = Array(repeating: Array(repeating: 0, count: c), count: r)

for i in 0..<r {
//	let line = testCase[i+1].split(separator: " ").map{ Int(String($0))! }
	let line = readLine()!.split(separator: " ").map { Int(String($0))! }
	map[i] = line
}
var copyMap = map

let dx = [1, 0, -1, 0]
let dy = [0, 1, 0, -1]

var success = false
var index = 0
var year = 0

func checkcMelting(_ iceMap : inout [[Int]], originMap: [[Int]], i: Int, j: Int) {
	for k in 0..<4 {
		let nx = i + dx[k]
		let ny = j + dy[k]
		
		if nx >= 0 && ny >= 0 && nx < r && ny < c && originMap[nx][ny] > 0 && iceMap[nx][ny] != 0 {
			iceMap[nx][ny] -= 1
		}
	}
}

func bfs(_ i: Int, _ j: Int, _ visit: inout [[Bool]]) {
	var queue = [(Int, Int)]()
	index = 0
	queue.append((i, j))
	visit[i][j] = true
	while index < queue.count {
		let position = queue[index]
		
		for k in 0..<4 {
			let nx = position.0 + dx[k]
			let ny = position.1 + dy[k]
			
			if nx >= 0 && ny >= 0 && nx < r && ny < c && map[nx][ny] > 0 && !visit[nx][ny] {
				queue.append((nx, ny))
				visit[nx][ny] = true
			}
		}
		index += 1
	}
}

func checkIceMountain() -> Bool {
	var iceMountain = 0
	var visit = Array(repeating: Array(repeating: false, count: c), count: r)
	
	for i in 0..<r {
		for j in 0..<c {
			if map[i][j] > 0 && !visit[i][j] {
				iceMountain += 1
				bfs(i, j, &visit)
			}
		}
	}
	
//	for row in visit {
//		print(row)
//	}
//	print()
	
	if iceMountain >= 2 {
		return true
	} else {
		return false
	}
}


while !success {
	var numberOfZero = 0
	year += 1
	
	for i in 0..<r {
		for j in 0..<c {
			if map[i][j] == 0 {
				checkcMelting(&copyMap, originMap: map, i: i, j: j)
				numberOfZero += 1
			}
		}
	}
	
//	for row in copyMap {
//		print(row)
//	}
//	print()
	
	map = copyMap
	if checkIceMountain() {
		success = true
		print(year)
		break
	}
	
	if numberOfZero == r * c {
		print(year)
		break
	}
}

