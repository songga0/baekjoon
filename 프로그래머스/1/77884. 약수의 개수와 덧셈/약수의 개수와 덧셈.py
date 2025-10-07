def solution(left, right):
    answer = 0
    result=[]
    num1=0
    num2=0
    for i in range(left,right+1):
        res=0
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                if j==i**0.5:
                    res+=1
                else:
                    res+=2
        if res%2==0:
            answer+=i
        else:
            answer-=i
    return answer