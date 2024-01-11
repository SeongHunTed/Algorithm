//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/11/24.
//

import Foundation

let info = readLine()!.split(separator: " ").map { Int(String($0))! }
let c = info[0]
let r = info[1]
let h = info[2]

let dx = [1, 0, -1, 0, 0, 0]
let dy = [0, 1, 0, -1, 0, 0]
let dz = [0, 0, 0, 0, 1, -1]

var day = -1
var index = 0
var queue = [(Int, Int, Int)]()

var boxes = Array(repeating: Array(repeating: [0], count: r), count: h)

for i in 0..<h {
	for j in 0..<r {
		boxes[i][j] = readLine()!.split(separator: " ").map { Int(String($0))! }
		for k in 0..<c {
			if boxes[i][j][k] == 1 {
				queue.append((i, j, k))
			}
		}
	}
}

func iJustWannaDeliciousTomatoes() -> Int {
	while index < queue.count {
		let startIndex = index
		let endIndex = queue.count
		day += 1
		for j in startIndex..<endIndex {
			let position = queue[j]
			
			for i in 0..<6 {
				let nz = position.0 + dz[i]
				let nx = position.1 + dx[i]
				let ny = position.2 + dy[i]
				
				if nx >= 0 && ny >= 0 && nz >= 0 && nx < r && ny < c && nz < h && boxes[nz][nx][ny] == 0 {
					boxes[nz][nx][ny] = 1
					queue.append((nz, nx, ny))
				}
			}
			index += 1
		}
	}
	return day
}


let result = iJustWannaDeliciousTomatoes()

for box in boxes {
	for row in box {
		for col in row {
			if col == 0 {
				print(-1)
				exit(0)
			}
		}
	}
}

print(result)

