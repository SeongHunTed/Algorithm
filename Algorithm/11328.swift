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

func ctoi(_ s: Character) -> Int {
    return Int(s.asciiValue!) - Int(UnicodeScalar("a").value)
}

func solution(_ str: String) -> String {
    let arr = str.components(separatedBy: " ")
    let str1 = arr[0]
    let str2 = arr[1]
    
    var checkArr = Array(repeating: 0, count: 26)
    
    if str1.count != str2.count {
        return "Impossible"
    }
        
    for s in str1 {
        checkArr[ctoi(s)] += 1
    }
    
    for s in str2 {
        if checkArr[ctoi(s)] == 0 {
            return "Impossible"
        } else {
            checkArr[ctoi(s)] -= 1
        }
    }
    
    return "Possible"
}

for _ in 0..<N {
    print(solution(readLine()!))
}
