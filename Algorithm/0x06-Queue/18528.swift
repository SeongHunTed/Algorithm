//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/18.
//

import Foundation

let testcase = Int(readLine()!)!
var queue: [Int?] = []
var front = 0
let file = FileIO()

for _ in 0..<testcase {
    let input = file.readString()
    
    switch input {
    case "push":
        let argv = Int(exactly: file.readInt())!
        queue.append(argv)
    case "pop":
        if queue.count == front {
            print(-1)
        } else {
            print(queue[front]!)
            front += 1
        }
    case "size":
        print(queue.count - front)
    case "empty":
        if queue.count == front {
            print(0)
        } else {
            print(1)
        }
    case "front":
        if queue[front] != nil {
            print(queue[front]!)
        } else {
            print("-1")
        }
    default:
        if let item = queue.last {
            print(item!)
        } else {
            print("-1")
        }
    }
 
}
