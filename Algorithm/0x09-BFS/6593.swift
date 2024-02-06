//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 1/16/24.
//

import Foundation

typealias Coord = (Int, Int, Int)

let dz = [0, 0, 0, 0, 1, -1]
let dx = [1, 0 , -1, 0, 0, 0]
let dy = [0, 1, 0, -1, 0, 0]

func bfs(_ start: Coord, _ end: Coord, _ apart: [[[String]]], _ check: inout [[[Int]]], _ boarder: Coord) {
	var queue = [Coord]()
	queue.append(start)
	check[start.0][start.1][start.2] = 1
	var index = 0
	
	while index < queue.count {
		let position = queue[index]
		index += 1
		
		for i in 0..<6 {
			let nz = position.0 + dz[i]
			let nx = position.1 + dx[i]
			let ny = position.2 + dy[i]
			
			if nz >= 0 && nx >= 0 && ny >= 0 && nz < boarder.0 && nx < boarder.1 && ny < boarder.2 && check[nz][nx][ny] == 0 {
				if apart[nz][nx][ny] == "." || apart[nz][nx][ny] == "E" {
					queue.append((nz, nx, ny))
					check[nz][nx][ny] = check[position.0][position.1][position.2] + 1
				}
			}
		}
	}
}

while true {
	let input = readLine()!.split(separator: " ").map { Int(String($0))! }
	let layer = input[0]
	let row = input[1]
	let col = input[2]
	
	if layer == 0 && row == 0 && col == 0 {
		break
	}
	
	var apart = Array(
		repeating: Array(repeating: [String](), count: row),
		count: layer
	)
	
	var check = Array(
		repeating: Array(
			repeating:
				Array(repeating: 0, count: col)
			, count: row),
		count: layer
	)
	
	for i in 0 ..< layer {
		for j in 0 ..< row {
			let input = Array(readLine()!).map { String($0) }
			apart[i][j].append(contentsOf: input)
		}
		_ = readLine()!
	}
	
	var start = Coord(0, 0, 0)
	var exit = Coord(0, 0, 0)
	
	for z in 0..<layer {
		for x in 0..<row {
			for y in 0..<col {
				if apart[z][x][y] == "S" {
					start = Coord(z, x, y)
				}
				
				if apart[z][x][y] == "E" {
					exit = Coord(z, x, y)
				}
			}
		}
	}
	bfs(start, exit, apart, &check, Coord(layer, row, col))
	let second = check[exit.0][exit.1][exit.2]
	
	if second != 0 {
		print("Escaped in \(second) minute(s).")
	} else {
		print("Trapped!")
	}
}
