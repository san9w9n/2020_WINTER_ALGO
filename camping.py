def check(l,p,v):
    camping = 0
    first = l * (v//p)
    last = v%p

    if last > l:
        camping = first + l
    else:
        camping = first + last
    return camping

case = 1
while True:
    avail, total, vacation = map(int,input().split())
    if avail==total==vacation==0: break
    print("Case {}: {}".format(case,check(avail,total,vacation)))
    case += 1
    

