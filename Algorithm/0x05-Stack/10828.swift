//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/16.
//

import Foundation

let testcase = Int(readLine()!)!
var stack: [Int] = []

for _ in 0..<testcase {
    let input = readLine()!.components(separatedBy: " ")
    
    switch input[0] {
    case "push":
        let argv = Int(input[1])!
        stack.append(argv)
    case "pop":
        if let last = stack.popLast() {
            print(last)
        } else {
            print("-1")
        }
    case "size":
        print(stack.count)
    case "empty":
        if stack.isEmpty {
            print("1")
        } else {
            print("0")
        }
    case "top":
        if stack.last != nil {
            print(stack.last!)
        } else {
            print("-1")
        }
    default:
        exit(1)
    }
    
}
