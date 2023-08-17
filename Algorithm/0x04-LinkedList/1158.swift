//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/16.
//

import Foundation

let inputs = readLine()!.components(separatedBy: " ")
let N = Int(inputs[0])!
let K = Int(inputs[1])!

var people = Array(repeating: 1, count: N+1)
people[0] = 0

func peopleSum() -> Int {
    
    let sum = people.reduce(0) { sum, item in
        sum + item
    }
    return sum
}

var index = 0
var results = [Int]()

while peopleSum() != 0 {
    for _ in 0..<K {
        index += 1
        if index > N {
            index = index - N
        }
        
        if people[index] == 0 {
            while true {
                index += 1
                if index > N {
                    index = index - N
                }
                if people[index] != 0 {
                    break
                }
            }
        }
    }
    
    people[index] = 0
    results.append(index)
}

let result = "<" + results.map { String($0) }.joined(separator: ", ") + ">"
print(result)
