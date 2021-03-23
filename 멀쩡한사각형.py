def gcd(n,m):
    if n==1 or m==1: return 1
    while n!=0:
        n,m=m%n,n
    return m

def solution(w,h):
    answer = 1
    w,h=min(w,h),max(w,h)
    if w==h: return w*h-w
    else:
        g=gcd(w,h)
        mw,mh=w//g,h//g
        arr=[]
        ans=[]
        for i in range(mw+1):
            arr.append(int(-(mh/mw)*i + mh))
        for i in range(len(arr)-1):
            sub = arr[i]-arr[i+1]
            if i!=len(arr)-2:
                for j in range(sub):
                    if j==sub-1:
                        ans.append(2)
                    else: ans.append(1)
            else:
                for j in range(sub):
                    ans.append(1)
        answer=(h*w)-((h//mh)*sum(ans))
    return answer