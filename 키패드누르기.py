#1,4,7 누를 때는 왼손 엄지
#3,6,9 누를 때는 오른손 엄지
#2,5,8,0 을 누를 때는 더 가까운 엄지(두 엄지손가락의 거리가 같을때는, 주 손잡이)

def solution(numbers, hand):
    answer = ''
    #스택으로 구현해서 마지막 인덱스가 현재 손가락의 위치
    left_hand=[10]
    right_hand=[12]
    
    for num in numbers:
        if num==1 or num==4 or num==7:
            answer+="L"
            left_hand.append(num)
        elif num==3 or num==6 or num==9:
            answer+="R"
            right_hand.append(num)
        else:
            if num==0: num=11
            i=(num-1)//3
            j=(num-1)%3
            li=(left_hand[-1]-1)//3 
            lj=(left_hand[-1]-1)%3
            ri=(right_hand[-1]-1)//3 
            rj=(right_hand[-1]-1)%3
            
            if abs(i-li)+abs(j-lj) > abs(i-ri)+abs(j-rj):
                right_hand.append(num)
                answer+="R"
            elif abs(i-li)+abs(j-lj) < abs(i-ri)+abs(j-rj):
                left_hand.append(num)
                answer+="L"
            else:
                if hand=="right":
                    right_hand.append(num)
                    answer+="R"
                else:
                    left_hand.append(num)
                    answer+="L"
                
    return answer