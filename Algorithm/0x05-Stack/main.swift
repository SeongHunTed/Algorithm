//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/17.
//

import Foundation

let testcase = Int(readLine()!)!
var stack: [Int] = []

for _ in 0..<testcase {
    let input = Int(readLine()!)!
    
    if input != 0 {
        stack.append(input)
    } else {
        stack.removeLast()
    }
}

print(stack.reduce(0, +))
