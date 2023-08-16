//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/14.
//

import Foundation

var str = readLine()!
var rightSide = ""
let M = Int(readLine()!)!

for _ in 0..<M {
    let command = readLine()!
    
    switch command {
    case "L":
        moveLeft()
    case "D":
        moveRight()
    case "B":
        delete()
    default:
        let argv = command.last!
        add(argv)
    }
}

let result: String = {
    let first = str
    let second = rightSide.reversed()
    return first + second
}()

print(result)

func moveLeft() {
    if !str.isEmpty {
        rightSide.append(str.removeLast())
    }
}

func moveRight() {
    if !rightSide.isEmpty {
        str.append(rightSide.removeLast())
    }
}

func delete() {
    if !str.isEmpty {
        str.removeLast()
    }
}

func add(_ argv: Character) {
    str.append(argv)
}
