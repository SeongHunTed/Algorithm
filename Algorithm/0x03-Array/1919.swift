//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/14.
//

import Foundation

var str1 = readLine()!
var str2 = readLine()!

var result = Array(repeating: 0, count: 26)

func ctoi(_ s: Character) -> Int {
    return Int(s.asciiValue!) - Int(UnicodeScalar("a").value)
}

for char in str1 {
    result[ctoi(char)] += 1
}

for char in str2 {
    result[ctoi(char)] -= 1
}

let sol = result.reduce(0) { sum, item in
    sum + abs(item)
}
print(sol)
