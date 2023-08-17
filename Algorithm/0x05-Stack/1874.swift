//
//  File.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/17.
//

import Foundation

let testcase = Int(readLine()!)!
var stack: [Int] = []
var result = ""
var count = 1

for _ in 0..<testcase {
    let input = Int(readLine()!)!
    
    while count <= input {
        push(count)
    }
    
    if stack.last! == input {
        pop()
    } else {
        print("NO")
        exit(0)
    }

}

for r in result {
    print(r)
}
                  
func push(_ i: Int) {
    stack.append(i)
    count += 1
    result.append("+")
}

func pop() {
    stack.removeLast()
    result.append("-")
}
                  
                  
