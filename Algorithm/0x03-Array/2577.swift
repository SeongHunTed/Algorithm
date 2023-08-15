//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/13.
//

import Foundation

var inputs: [Int] = []

for _ in 0..<3 {
    inputs.append(Int(readLine()!)!)
}

let multipled = String(inputs.reduce(1, *))
var result = [Character: Int]()

for item in multipled {
    result[item, default: 0] += 1
}

let numbers = "0123456789"
for number in numbers {
    print(result[number, default: 0])
}
