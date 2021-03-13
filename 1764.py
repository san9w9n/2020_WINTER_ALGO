import sys
n,m=map(int,sys.stdin.readline().split())
notlisten=set()
notsee=set()
for _ in range(n):
    notlisten.add(sys.stdin.readline().rstrip())
for _ in range(m):
    notsee.add(sys.stdin.readline().rstrip())

seelisten = sorted(list(notlisten.intersection(notsee)))

print(len(seelisten))
for s in seelisten:
    print(s)

