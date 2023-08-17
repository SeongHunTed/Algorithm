//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/17.
//

import Foundation

let N = Int(readLine()!)!
var arr = readLine()!
    .components(separatedBy: " ")
    .map { Int($0)! }
var stack: [Int] = []

var results = Array(repeating: -1, count: N)

for (index, item) in arr.enumerated() {
    
    while !stack.isEmpty && arr[stack.last!] < item {
        results[stack.removeLast()] = item
    }
    
    stack.append(index)
}

print(results)
