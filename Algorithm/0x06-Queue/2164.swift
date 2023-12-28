//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/18.
//

import Foundation

let N = Int(readLine()!)!

var queue: [Int] = []
var front = 0

for i in 1...N {
    queue.append(i)
}

while queue[front] != 0 {

    let item = queue[front]
    queue[front] = 0
    front += 1
    if queue.count == front {
        print(item)
        break
    }
    queue.append(queue[front])
    queue[front] = 0
    front += 1
}


