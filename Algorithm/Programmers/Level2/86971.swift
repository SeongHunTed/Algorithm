import Foundation

func solution(_ n:Int, _ wires:[[Int]]) -> Int {
    var result = Int.max
    var networks: [[Int]] = Array(repeating: [], count: n+1)
    var visited = Array(repeating: false, count: n+1)
    var count = 1
    
    func dfs(graph: [[Int]], v: Int) {
        for i in 0..<graph[v].count {
            let vertex = graph[v][i]
            if !visited[vertex]  {
                visited[vertex] = true
                count += 1
                dfs(graph: graph, v: graph[v][i])
            }
        }
    }
    
    for i in 0..<wires.count {
        let a = wires[i][0], b = wires[i][1]
        networks[b].append(a)
        networks[a].append(b)
    }
    
    for i in 0..<wires.count {
        var graph = networks
        let a = wires[i][0], b = wires[i][1]
        let index1 = graph[b].firstIndex(of: a)!
        graph[b].remove(at: index1)
        let index2 = graph[a].firstIndex(of: b)!
        graph[a].remove(at: index2)
        
        visited = Array(repeating: false, count: n+1)
        visited[1] = true
        count = 1
        dfs(graph: graph, v: 1)
        
        let anotherTopCount = abs(n-count)
        result = min(result, abs(count-anotherTopCount))
    }
    
    return result
}