import sys
N=int(sys.stdin.readline())

#홀수번째 원소는 하얀색
#짝수번째 원소는 파랑색
tri=[-1,1,1,1,2,2,3,4,5]+[0]*92
def P(k):
    if 1<=k<=3: return 1
    if 4<=k<=5: return 2
    if k==6: return 3
    if k==7: return 4
    if k==8: return 5
    if tri[k]==0:
        tri[k]=P(k-5)+P(k-1)
        return tri[k]
    else:
        return tri[k]
P(100)
for _ in range(N):
    T=int(sys.stdin.readline())
    print(tri[T])