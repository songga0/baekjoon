def solution(cards1, cards2, goal):
    for i in goal:
        if len(cards1)>0 and i==cards1[0]:
            cards1=cards1[1:]
        elif len(cards2)>0 and i==cards2[0]:
            cards2=cards2[1:]
        else:
            return "No"
    return "Yes"