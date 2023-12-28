//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/10/03.
//

import Foundation

let N = Int(readLine()!)!
var result = 0
var stack: [Character] = []

for _ in 0..<N {
    stack = []
    let input = readLine()!
    
    for s in input {
        if let top = stack.last, top == s {
            stack.removeLast()
        } else {
            stack.append(s)
        }
    }
    
    print("input: \(input) / stack: \(stack)")
    
    if stack.isEmpty {
        result += 1
    }
}

print(result)

