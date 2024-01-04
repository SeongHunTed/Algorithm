//
//  4949.swift
//  Algorithm
//
//  Created by Hoon on 1/4/24.
//

import Foundation

var sentence = ""

while true {
	sentence = readLine()!
	if sentence == "." { break }
	var stack = [Character]()
	var result = true
	
	for char in sentence {
		if char == "[" || char == "(" { stack.append(char) }
		else if char == "]" || char == ")" {
			if stack.isEmpty { result = false; break }
			if char == "]" && stack.removeLast() != "[" { result = false; break }
			if char == ")" && stack.removeLast() != "(" { result = false; break }
		}
	}
	
	if result == false { print("no") }
	else {
		if !stack.isEmpty { print("no") }
		else { print("yes") }
	}
}
