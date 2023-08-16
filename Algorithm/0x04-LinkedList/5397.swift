//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/16.
//

import Foundation

let testcase = Int(readLine()!)!
var str = ""
var leftSpace = ""
var rightSpace = ""

for _ in 0..<testcase {
    str = readLine()!
    leftSpace = ""
    rightSpace = ""
    
    for char in str {
        switch char {
        case "<":
            swiftLeft()
        case ">":
            swiftRight()
        case "-":
            backSpace()
        default:
            leftSpace.append(char)
        }
    }
    print(leftSpace + rightSpace.reversed())
}



func swiftLeft() {
    if !leftSpace.isEmpty {
        rightSpace.append(leftSpace.removeLast())
    }
}

func swiftRight() {
    if !rightSpace.isEmpty {
        leftSpace.append(rightSpace.removeLast())
    }
}

func backSpace() {
    if !leftSpace.isEmpty {
        leftSpace.removeLast()
    }
}
