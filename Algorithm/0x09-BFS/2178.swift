//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/9/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let m = input[1]

var miro = Array(repeating: [0], count: n)

for i in 0..<n {
	let line = Array(readLine()!).map { Int(String($0))! }
	miro[i] = line
}

func escape(_ miro: [[Int]]) -> Int {
	var visit = Array(repeating: Array(repeating: 0, count: m), count: n)
	var queue = [(Int, Int)]()
	visit[0][0] = 1
	let dx = [1, -1, 0, 0]
	let dy = [0, 0, -1, 1]
	
	queue.append((0, 0))
	
	while !queue.isEmpty {
		let prevPosition = queue.removeFirst()
		
		for k in 0..<4 {
			let nx = prevPosition.0 + dx[k]
			let ny = prevPosition.1 + dy[k]
			
			if nx >= 0 && ny >= 0 && nx < n && ny < m && miro[nx][ny] == 1 && visit[nx][ny] == 0 {
				visit[nx][ny] = visit[prevPosition.0][prevPosition.1] + 1
				queue.append((nx, ny))
			}
		}
	}
	
	return visit[n-1][m-1]
}

let result = escape(miro)
print(result)
