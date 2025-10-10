import heapq

def solution(n, works):
    answer = 0
    for i in range(len(works)):
        works[i]*=-1
    heapq.heapify(works)
    for i in range(n):
        x=heapq.heappop(works)
        if x==0:
            break
        heapq.heappush(works, x + 1)
    return sum(w ** 2 for w in works)