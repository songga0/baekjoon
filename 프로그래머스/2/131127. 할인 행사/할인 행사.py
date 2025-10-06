def solution(want, number, discount):
    answer = []
    result=0
    day=len(discount)-9
    for i in range(day):
        answer.append(discount[i:i+10])
    for i in answer:
        check=True
        for j in range(len(want)):
            if i.count(want[j])<number[j]:
                check=False
                break
        if check==True:
            result+=1
    return result