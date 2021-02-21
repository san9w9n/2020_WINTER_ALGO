import sys
x,y=map(int,sys.stdin.readline().split())
a,b=x,y
#gcd.
while b!=0:
    a=a%b 
    a,b=b,a
print(a)
#최소공배수== 두수곱//최대공약수
print((x*y)//a)