from collections import deque

def change(word1,word2):
    count=0
    for i,j in zip(word1, word2):
        if i!=j:
            count+=1
    return count


def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin, 0))
    visited=set()
    while queue:
        word, count = queue.popleft()
        if word == target:
                return count

        for i in words:
                if i not in visited and change(word, i) == 1:
                    visited.add(word)
                    queue.append((i, count + 1))
