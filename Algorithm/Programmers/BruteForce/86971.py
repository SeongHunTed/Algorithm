import math
import sys
sys.setrecursionlimit(10 ** 6)

def countDepth(start, graphs, visited):
    count = 1
    visited[start] = True
    for item in graphs[start]:
        if not visited[item]:
            count += countDepth(item, graphs, visited)
    return count

def solution(n, wires):
    
    minimumDifference = 999999
    graphs = [[] for _ in range(n+1)]
    check = [[True] * (n+1) for _ in range(n+1)]
    
    for wire in wires:
        u, v = wire[0], wire[1]
        graphs[u].append(v)
        graphs[v].append(u)
        
    for wire in wires:
        visited = [False] * (n+1)
        u, v = wire[0], wire[1]
        graphs[u].remove(v)
        graphs[v].remove(u)
        
        count1 = countDepth(u, graphs, visited)
        count2 = countDepth(v, graphs, visited)
        
        minimumDifference = min(minimumDifference, abs(count1 - count2))
        
        graphs[u].append(v)
        graphs[v].append(u)
    
        
    return minimumDifference