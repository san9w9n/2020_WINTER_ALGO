import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x,y=map(int,sys.stdin.readline().split())
    d = y-x
    if d<=3:
        print(d)
        continue
    elif d==4:
        print(3)
    else:
        i=2
        while True:
            if i**2 < d <= (i**2)+i:
                print(2*i)
                break
            elif (i**2)+i < d <= (i+1)**2:
                print(i+i+1)
                break
            i+=1
            
                

            

        
        
