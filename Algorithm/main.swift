//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/14.
//

import Foundation

let N = Int(readLine()!)!
let arr = readLine()!.components(separatedBy: " ").map { Int($0)! }
let v = Int(readLine()!)!

var dict = [Int: Int]()

arr.forEach { item in
    dict[item, default: 0] += 1
}

print(dict[v, default: 0])
