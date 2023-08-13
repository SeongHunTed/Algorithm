//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/13.
//

import Foundation

let S = readLine()!
var alphabetCounter: [Character: Int] = [:]

let alphabets = "abcdefghijklmnopqrstuvwxyz"

for char in S {
    alphabetCounter[char, default: 0] += 1
}

let result = alphabets.map { alphabetCounter[$0, default: 0] }
let resultString = result.map{ String($0) }.joined(separator: " ")
print(resultString)
