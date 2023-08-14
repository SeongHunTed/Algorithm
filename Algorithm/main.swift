//
//  main.swift
//  Algorithm
//
//  Created by Hoon on 2023/08/14.
//

import Foundation

//let N = Int(readLine()!)!
//var result = Array(repeating: true, count: N)
//let alphabets = "abcdefghijklmnopqrstuvwxyz"
//
//for i in 0..<N {
//    let inputs = readLine()!.split(separator: " ")
//    let string1 = inputs[0]
//    let string2 = inputs[1]
//
//    if string1.count != string2.count {
//        result[i] = false
//        continue
//    }
//
//    var arr = Array(repeating: 0, count: 26)
//    for (index, alphabet) in alphabets.enumerated() {
//        if string1.contains(alphabet) {
//            arr[index] += 1
//        }
//
//        if string2.contains(alphabet) {
//            arr[index] -= 1
//        }
//    }
//
//    for item in arr {
//        if item != 0 {
//            result[i] = false
//            break
//        }
//    }
//
//    if result[i] {
//        print("Possible")
//    } else {
//        print("Impossible")
//    }
//}

var N = Int(readLine()!)!

func solution(_ str: String) -> String {
    var arr = str.components(separatedBy: " ")
    var str1 = arr[0]
    var str2 = arr[1]
    
    for i in str2 {
        var n1 = 0
        var n2 = 0
        
        for j in str1 {
            if i == j { n1 += 1 }
        }
        
        for j in str2 {
            if i == j { n2 += 1 }
        }
        
        if n1 != n2 { return "Impossible" }
        else {
            str1 = str1.filter{ $0 != i }
            str2 = str2.filter{ $0 != i }
        }
    }
    
    return "Possible"
}

for _ in 0..<N {
    print(solution(readLine()!))
}
