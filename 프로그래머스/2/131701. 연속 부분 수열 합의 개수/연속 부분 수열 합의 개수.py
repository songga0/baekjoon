def solution(elements):
    answer = []
    l=len(elements)
    elements=elements*2
    for i in range(1,l+1):
        for j in range(1,l+1):
            answer.append(sum(elements[i:i+j]))
    answer=list(set(answer))
    return len(answer)