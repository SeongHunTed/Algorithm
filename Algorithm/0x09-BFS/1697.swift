//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/11/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
var subin = input[0]
let sister = input[1]

var time = 0
var queue = Deque<Int>()
var visit = Set<Int>()
visit.insert(subin)
queue.pushRight(subin)
let dx = [-1, 1, 2]

func letsGetIt() -> Int {
	if subin == sister { return 0 }
	while true {
		time += 1
		for _ in 0..<queue.count {
			let position = queue.popLeft()
			
			for i in 0..<3 {
				if i == 2 {
					subin = position * dx[i]
				} else {
					subin = position + dx[i]
				}
				
				if subin == sister { return time }
				
				if subin >= 0 && subin < 100001 && !visit.contains(subin) {
					queue.pushRight(subin)
					visit.insert(subin)
				}
			}
		}
	}
}

print(letsGetIt())
