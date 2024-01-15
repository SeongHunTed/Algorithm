//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/16/24.
//

import Foundation

let n = Int(readLine()!)!

var map = Array(repeating: [0], count: n)
var copyMap = map
var visit = Array(repeating: Array(repeating: false, count: n), count: n)

var maxArea = 1
var minHeight = 999999
var maxHeight = 0

for i in 0..<n {
	map[i] = readLine()!.split(separator: " ").map {
		let height = Int(String($0))!
		minHeight = min(minHeight, height)
		maxHeight = max(maxHeight, height)
		return height
	}
}

func checkArea(_ i: Int, _ j: Int, _ rain: Int) {
	var queue = [(i, j)]
	var index = 0
	visit[i][j] = true
	
	let dx = [1, 0, -1, 0]
	let dy = [0, 1, 0, -1]
	
	while index < queue.count {
		let position = queue[index]
		
		for k in 0..<4 {
			let nx = position.0 + dx[k]
			let ny = position.1 + dy[k]
			
			if nx >= 0 && ny >= 0 && nx < n && ny < n && !visit[nx][ny] && map[nx][ny] > rain {
				visit[nx][ny] = true
				copyMap[nx][ny] = -1
				queue.append((nx, ny))
			}
		}
		index += 1
	}
}


for rain in minHeight..<maxHeight {
	copyMap = map
	for i in 0..<n {
		for j in 0..<n {
			if copyMap[i][j] <= rain {
				copyMap[i][j] = -1
			}
		}
	}
	visit = Array(repeating: Array(repeating: false, count: n), count: n)
	
	var area = 0
	for i in 0..<n {
		for j in 0..<n {
			if copyMap[i][j] > 0 {
				checkArea(i, j, rain)
				area += 1
			}
		}
	}
	maxArea = max(maxArea, area)
}

print(maxArea)
