T = int(input())   # 유클리드 호제법
for i in range(T):  
    a, b = map(int,input().split())
    x, y = a, b
    while y != 0:   # y가 0이 아니면 계속 반복
        temp = x  # temp = 6, 10, 6, 4
        x = y     # x = 10, 6, 4, 2
        y = temp % y  # y = 6, 4, 2, 0
    print(a * b // x)    # 최소공배수 = 두 자연수의 곱 / 최대공약수