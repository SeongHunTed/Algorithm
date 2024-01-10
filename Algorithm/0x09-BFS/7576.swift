//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/10/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0] // 6
let m = input[1] // 4

var box = Array(repeating: [0], count: m)

for i in 0..<m {
	let line = readLine()!.split(separator: " ").map { Int(String($0))! }
	box[i] = line
}

func howManyDayNeedToEarTomatoes(_ box: [[Int]]) -> Int {
	let dx = [1, 0, -1, 0]
	let dy = [0, 1, 0, -1]
	var queue = Deque<(Int, Int)>()
	var days = -1
	var todayBox = box
	
	for i in 0..<m {
		for j in 0..<n {
			if todayBox[i][j] == 1 {
				queue.pushRight((i, j))
			}
		}
	}
	
	while !queue.isEmpty {
		for _ in 0..<queue.count {
			let position = queue.popLeft()
			for k in 0..<4 {
				let nx = position.0 + dx[k]
				let ny = position.1 + dy[k]
				
				if nx >= 0 && ny >= 0 && nx < m && ny < n && todayBox[nx][ny] == 0 {
					todayBox[nx][ny] = 1
					queue.pushRight((nx, ny))
				}
			}
		}
		days += 1
	}

	for row in todayBox {
		if row.contains(0) {
			days = -1
		}
	}
	
	return days
}

print(howManyDayNeedToEarTomatoes(box))
