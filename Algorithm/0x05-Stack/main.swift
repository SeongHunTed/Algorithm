//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/17.
//

import Foundation

let towerCount = Int(readLine()!)!
var towers = readLine()!.components(separatedBy: " ").map { Int($0)!}
var results = Array(repeating: 0, count: towerCount)
var stack: [(index: Int, height: Int)] = []

for (index, tower) in towers.enumerated() {
    
    while !stack.isEmpty && stack.last!.height < tower {
        stack.removeLast()
    }
    
    if let top = stack.last {
        results[index] = top.index + 1
    }
    
    stack.append((index, tower))
}

print(results.map { String($0) }.joined(separator: " "))

