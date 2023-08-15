//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/13.
//

import Foundation

let roomNumber = readLine()!

var setCounter = Array(repeating: 0, count: 10)

for num in roomNumber {
    if ["6", "9"].contains(num) {
        setCounter[6] += 1
    } else {
        setCounter[Int(String(num))!] += 1
    }
}

setCounter[6] = (setCounter[6] + 1) / 2
print(setCounter.max()!)
