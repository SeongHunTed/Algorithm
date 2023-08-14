//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/14.
//

//import Foundation
//
//let inputs = readLine()!.components(separatedBy: " ").map { Int($0)! }
//let N = inputs[0], K = inputs[1]
//
//var boys = [Int: Int]()
//var girls = [Int: Int]()
//var roomCount = 0
//
//for _ in 0..<N {
//    let info = readLine()!.components(separatedBy: " ").map { Int($0)! }
//    let sex = info[0]
//    let grade = info[1]
//
//    if sex == 0 {
//        girls[grade, default: 0] += 1
//    } else {
//        boys[grade, default: 0] += 1
//    }
//}
//
//for i in 1...6 {
//    if girls[i] != nil {
//        if girls[i]! % K != 0 {
//            roomCount += 1
//        }
//        roomCount += girls[i]! / K
//    }
//
//    if boys[i] != nil {
//        if boys[i]! % K != 0 {
//            roomCount += 1
//        }
//        roomCount += boys[i]! / K
//    }
//}
//
//print(roomCount)

import Foundation

let inputs = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = inputs[0], K = inputs[1]

var students = Array(repeating: [0, 0], count: 7)  // [0]은 여학생 수, [1]은 남학생 수
var roomCount = 0

for _ in 0..<N {
    let info = readLine()!.split(separator: " ").compactMap { Int($0) }
    let sex = info[0], grade = info[1]
    students[grade][sex] += 1
}

print(students)

for student in students {
    roomCount += (student[0] + K - 1) / K + (student[1] + K - 1) / K
}

print(roomCount)
