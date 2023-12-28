//
//  10809.swift
//  Algorithm
//
//  Created by Hoon on 12/28/23.
//

import Foundation

let inputWord = readLine()!
let inputWordArray = Array(inputWord).map { String($0) }
var alphabetDictionary: [String: Int] = [:]

let alphabet = "abcdefghijklmnopqrstuvwxyz"
let alphabetArray = Array(alphabet).map { String($0) }

var indexResult = Array(repeating: -1, count: alphabetArray.count)
var counter = 0

inputWordArray.forEach {
	guard let indexOfAlphabet = alphabetArray.firstIndex(of: $0) else { exit(0) }
	if let preCounter = alphabetDictionary[$0] {
		indexResult[indexOfAlphabet] = preCounter
	} else {
		alphabetDictionary[$0] = counter
		indexResult[indexOfAlphabet] = counter
	}
	counter += 1
}

print(indexResult.map { String($0) }.joined(separator: " "))
