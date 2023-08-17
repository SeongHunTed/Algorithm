//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/18.
//

import Foundation

let testcase = Int(readLine()!)!
var queue: [Int] = []

for _ in 0..<testcase {
    let input = readLine()!.components(separatedBy: " ")
    
    switch input[0] {
    case "push":
        let argv = Int(input[1])!
        queue.append(argv)
    case "pop":
        if !queue.isEmpty {
            print(queue.removeFirst())
        } else {
            print("-1")
        }
    case "size":
        print(queue.count)
    case "empty":
        if queue.isEmpty {
            print("1")
        } else {
            print("0")
        }
    case "front":
        if let item = queue.first {
            print(item)
        } else {
            print("-1")
        }
    default:
        if let item = queue.last {
            print(item)
        } else {
            print("-1")
        }
    }
    
}
