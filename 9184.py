import sys
w_list={(i,j,k):-1 for i in range(21) for j in range(21) for k in range(21)}
def func(a,b,c):
    if a==0 or b==0 or c==0:
        w_list[(a,b,c)]=1
        return 1
    else:
        if w_list.get((a,b,c)) != -1:
            return w_list.get((a,b,c))
        else:
            if a<b<c:
                w_list[(a,b,c)]=func(a,b,c-1)+func(a,b-1,c-1)-func(a,b-1,c)
                return w_list.get((a,b,c))
            else:
                w_list[(a,b,c)]=func(a-1,b,c)+func(a-1,b-1,c)+func(a-1,b,c-1)-func(a-1,b-1,c-1)
                return w_list.get((a,b,c))
for i in range(21):
    for j in range(21):
        for k in range(21):
            func(i,j,k)
while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1: sys.exit(0)
    if a<=0 or b<=0 or c<=0:
        print("w({}, {}, {}) = {}".format(a,b,c,1))
    elif a>20 or b>20 or c>20:
        print("w({}, {}, {}) = {}".format(a,b,c,w_list.get((20,20,20))))
    else: 
        print("w({}, {}, {}) = {}".format(a,b,c,w_list.get((a,b,c)))) 