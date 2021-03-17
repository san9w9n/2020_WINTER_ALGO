stack=[]

def check():
    global stack
    if len(stack)>=2:
        if stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
            return True
        else: return False
    return False


def solution(board, moves):
    global stack
    answer = 0
    n=len(board[0])
    for move in moves:
        for i in range(n):
            if board[i][move-1]!=0:
                stack.append(board[i][move-1])
                print(*stack)
                board[i][move-1]=0
                if check(): answer+=2
                print(*stack)
                break
    return answer