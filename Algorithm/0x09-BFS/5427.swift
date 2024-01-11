//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/11/24.
//

import Foundation

let testCase = Int(readLine()!)!

let dx = [1, 0, -1, 0]
let dy = [0, 1, 0, -1]

for _ in 0..<testCase {
	let input = readLine()!.split(separator: " ").map { Int(String($0))! }
	let c = input[0]
	let r = input[1]
	
	var queue = [(Int, Int)]()
	var fireQueue = [(Int, Int)]()
	var miro = Array(repeating: [""], count: r)
	var visit = Array(repeating: Array(repeating: false, count: c), count: r)
	var success = false
	var index = 0
	var fireIndex = 0
	var count = 0
	var startWithEnd = false
	
	// 초기화
	for i in 0..<r {
		miro[i] = Array(readLine()!.map { String($0) })
		for (index, item) in miro[i].enumerated() {
			if item == "@" {
				queue.append((i, index))
				visit[i][index] = true
				miro[i][index] = "."
			}
			
			if item == "*" {
				fireQueue.append((i, index))
				miro[i][index] = "#"
			}
		}
	}
	
	while !success && index < queue.count && fireIndex <= fireQueue.count {
		for i in fireIndex..<fireQueue.count {
			let position = fireQueue[i]
			
			for j in 0..<4 {
				let nx = position.0 + dx[j]
				let ny = position.1 + dy[j]
				
				if nx >= 0 && ny >= 0 && nx < r && ny < c && miro[nx][ny] == "." {
					miro[nx][ny] = "*"
					miro[position.0][position.1] = "#"
					fireQueue.append((nx, ny))
				}
			}
			fireIndex += 1
		}
		
		for i in index..<queue.count {
			let position = queue[i]
			if position.0 == 0 || position.1 == 0 || position.0 == r - 1 || position.1 == c - 1 {
				startWithEnd = true
				success = true
				break
			}
			
			for j in 0..<4 {
				let nx = position.0 + dx[j]
				let ny = position.1 + dy[j]
				
				if (nx == 0 || ny == 0 || nx == r - 1 || ny == c - 1) && miro[nx][ny] == "." {
					success = true
				}
				
				if nx >= 0 && ny >= 0 && nx < r && ny < c && miro[nx][ny] == "." && !visit[nx][ny] {
					queue.append((nx, ny))
					miro[nx][ny] = "@"
					visit[nx][ny] = true
				}
			}
			index += 1
		}
		count += 1
	}
	
	if startWithEnd { print(1) }
	else { print(success ? count + 1 : "IMPOSSIBLE") }
}
