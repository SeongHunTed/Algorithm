//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/17.
//

import Foundation

let buildingCount = Int(readLine()!)!
var buildings: [Int] = []
var stack: [Int] = []
var results = 0
var counter = 0

for _ in 0..<buildingCount {
    buildings.append(Int(readLine()!)!)
}

for building in buildings {
    while !stack.isEmpty && stack.last! <= building {
        stack.removeLast()
    }
    results += stack.count
    stack.append(building)
}

print(results)
