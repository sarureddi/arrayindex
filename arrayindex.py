r1,k1=map(int,input().split())
f1=list(map(int,input().split()))
li1=[]
l1=[]
h1=[]
for i11 in range(0,k1):
    u1,v1=map(int,input().split())
    for i in range(u1,v1+1):
        li1.append(f1[i11-1])
    l1.append(sum(li1))
h1.append(l1[0])
for i11 in range(0,len(l1)-1):
    s1=l1[i11+1]-l1[i11]
    h1.append(s1)
for i11 in h1:
    print(i11)
