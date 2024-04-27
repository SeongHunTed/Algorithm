import Foundation

func isTransformable(_ a: String, _ b: String) -> Bool {
    var diffCount = 0
    let aWord = Array(a)
    let bWord = Array(b)
    
    for i in 0..<a.count {
        if aWord[i] != bWord[i] {
            diffCount += 1
        }
    }
    return diffCount == 1
}

func dfs(_ start: String, _ target: String, _ words: [String], _ count: Int, _ visited: inout [Bool]) -> Int {
    if start == target {
        return count
    }
    
    var result = Int.max
    for (index, word) in words.enumerated() {
        if !visited[index] {
            if isTransformable(word, start) {
                visited[index] = true
                result = min(dfs(word, target, words, count + 1, &visited), result)
                visited[index] = false
            }
        }
    }
    
    return result
}

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
    
    if !words.contains(target) {
        return 0
    }
    
    var results: [Int] = [Int]()
    
    for (index, word) in words.enumerated() {
        var visited = Array(repeating: false, count: words.count)
        if isTransformable(begin, word) {
            visited[index] = true
            results.append(dfs(word, target, words, 1, &visited))
            visited[index] = false
        }
    }
    
    return results.min()!
}