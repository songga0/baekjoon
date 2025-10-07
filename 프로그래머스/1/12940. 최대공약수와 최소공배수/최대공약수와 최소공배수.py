import math
def solution(n, m):
    answer = []
    x=math.gcd(n,m)
    answer.append(x)
    answer.append(x*(n//x)*(m//x))
    return answer