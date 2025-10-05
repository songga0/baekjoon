def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # 짝이면 제거
        else:
            stack.append(char)  # 짝이 아니면 넣기
    return 1 if len(stack) == 0 else 0  # 예: 모두 제거되면 0, 아니면 1
