import heapq
import sys

INF = int(1e9)

sys.stdin = open("미래도시.txt", "r")

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


result = dijkstra(1)[k]
distance = [INF] * (n + 1)
result += dijkstra(k)[x]

if result < INF:
    print(result)
else :
    print(-1)
