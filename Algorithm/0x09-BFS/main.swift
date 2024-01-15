//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/12/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let max = input[0] // F 10층
let gang = input[1] // S 1층
let startLink = input[2] // G 9층
let up = input[3] // U 2
let down = -input[4] // D 1
let direction = [up, down]

var success = false
var index = 0
var visit = Array(repeating: false, count: max + 1)

var count = 0
var queue = [gang]
visit[0] = true
visit[gang] = true

while !success && index < queue.count {
	for _ in 0..<queue.count - index {
		let position = queue[index]
		for i in 0..<2 {
			let next = position + direction[i]
			if next == startLink {
				success = true
			}
			
			if next > 0 && next <= max && !visit[next] {
				visit[next] = true
				queue.append(next)
			}
		}
		index += 1
	}
	count += 1
}

if gang == startLink {
	print(0)
} else if max - gang == 1 {
	print(1)
} else if !success {
	print("use the stairs")
} else {
	print(count)
}
