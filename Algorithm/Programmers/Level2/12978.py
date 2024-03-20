import heapq as hq

def dijkstra(start, graph, N):
    q = []
    distance = {i: float('inf') for i in range(1, N+1)}
    hq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        weight, currentNode = hq.heappop(q)
        
        if distance[currentNode] < weight:
            continue
            
        for nextNode in graph[currentNode]:
            dist = weight + nextNode[1]
            
            if dist < distance[nextNode[0]]:
                distance[nextNode[0]] = dist
                hq.heappush(q, (dist, nextNode[0]))
    
    return distance
        
# 다익스트라 푸는 법        
def solution(N, road, K):
    answer = 0
    graph = {i: [] for i in range(1, N+1)}
    
    for r in road:
        start, destination, time = r
        graph[start].append((destination, time))
        graph[destination].append((start, time))
    
    results = dijkstra(1, graph, N)
    
    for value in results.values():
        if value <= K:
            answer += 1
    
    return answer

## 플로이드와셜
def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        graph[i][i] = 0
    
    for r in road:
        start, destination, time = r
        graph[start][destination] = min(graph[start][destination], time)
        graph[destination][start] = min(graph[destination][start], time)
    
    # 플로이드 와샬
    for k in range(1, N+1):
        for start in range(1, N+1):
            for end in range(1, N+1):
                graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end] )
    print(graph[1])
    for item in graph[1]:
        if item <= K:
            answer += 1        
    
    return answer
