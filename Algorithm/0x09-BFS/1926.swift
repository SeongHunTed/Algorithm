//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/9/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0] // col
let M = input[1] // row

var painting: [[Int]] = Array(repeating: Array(repeating: 0, count: M), count: N)
var count = 0

for i in 0..<N {
	let line = readLine()!.split(separator: " ").map { Int($0)! }
	painting[i] = line
}

func countPaintings(_ sx: Int, _ sy: Int) -> Int {
	var area = 1
	var queue: [(Int, Int)] = [(sx, sy)]
	let dx = [-1, 1, 0, 0]
	let dy = [0, 0, 1, -1]
	
	painting[sx][sy] = 0
	while !queue.isEmpty {
		let position = queue.removeFirst()
		for i in 0..<4 {
			let nx = position.0 + dx[i]
			let ny = position.1 + dy[i]
			
			if (0..<N) ~= nx && (0..<M) ~= ny && painting[nx][ny] == 1 {
				area += 1
				painting[nx][ny] = 0
				queue.append((nx, ny))
			}
		}
	}
	
	return area
}

var maxWidth = 0

// i : col
// j : row
for i in 0..<N {
	for j in 0..<M {
		if painting[i][j] == 1 {
			count += 1
			maxWidth = max(maxWidth, countPaintings(i, j))
		}
	}
}

print(count)
print(maxWidth)
