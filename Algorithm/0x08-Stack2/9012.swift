//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/10/04.
//

import Foundation

let N = Int(readLine()!)!
var stack: [Character] = []

for _ in 0..<N {
    stack = []
    let string = String(readLine()!)
    
    for s in string {
        if s == "(" {
            stack.append(s)
        } else {
            if let pop = stack.last, pop == "(" {
                stack.removeLast()
            } else {
                stack.append(s)
                break
            }
        }
    }
    
    if stack.isEmpty {
        print("YES")
    } else {
        print("NO")
    }
}
