//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/18.
//

import Foundation

let N = Int(readLine()!)!
var people = [Int]()
var stack = [Int]()
var result = 0

for i in 0..<N {
    let person = Int(readLine()!)!
    people.append(person)
    
    while !stack.isEmpty && people[stack.last!] < person {
        stack.removeLast()
        result += stack.count
    }

    stack.append(i)
}

print(result)
