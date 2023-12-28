//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/18.
//

import Foundation

struct Deque<T> {
    var queue: [T?] = []
    private var frontIndex = 0
    
    var frontValue: T? {
        if isEmpty {
            return nil
        } else {
            return queue[frontIndex]!
        }
    }
    
    var rearValue: T? {
        if isEmpty {
            return nil
        } else {
            return queue.last!
        }
    }
    
    var isEmpty: Bool {
        if queue.isEmpty {
            return true
        }
        return queue[frontIndex] == nil
    }
    
    var size: Int {
        if queue[frontIndex] == nil {
            return 0
        }
        return queue.count - frontIndex
    }
    
    mutating func pushFront(_ value: T) {
        if frontIndex == 0 {
            queue.insert(value, at: 0)
        } else {
            frontIndex -= 1
            queue[frontIndex] = value
        }
    }
    
    mutating func pushBack(_ value: T) {
        queue.append(value)
    }
    
    mutating func popFront() -> T? {
        guard !isEmpty else { return nil }
        let item = queue[frontIndex]
        queue[frontIndex] = nil
        frontIndex += 1
        return item
    }
    
    mutating func popBack() -> T? {
        guard !isEmpty else { return nil }
        if size == 1 {
            frontIndex -= 1
        }
        let item = queue.removeLast()
        return item
    }
}


var deque = Deque<Int>()

let testcase = Int(readLine()!)!

for _ in 0..<testcase {
    let command = readLine()!.components(separatedBy: " ")
    
    switch command[0] {
    case "push_front":
        let num = Int(command[1])!
        deque.pushFront(num)
    case "push_back":
        let num = Int(command[1])!
        deque.pushBack(num)
    case "pop_front":
        if let front = deque.popFront() {
            print(front)
        } else {
            print(-1)
        }
    case "pop_back":
        if let last = deque.popBack() {
            print(last)
        } else {
            print(-1)
        }
    case "size":
        print(deque.size)
    case "empty":
        if deque.isEmpty == true {
            print(1)
        } else {
            print(0)
        }
    case "front":
        if let front = deque.frontValue {
            print(front)
        } else {
            print(-1)
        }
    case "back":
        if let last = deque.rearValue {
            print(last)
        } else {
            print(-1)
        }
    default:
        print("Fuck You")
    }
    
}

