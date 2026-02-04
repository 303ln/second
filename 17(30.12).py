f=open('17(30.12).txt')
s=[int(x) for x in f]
t=[]
p=[]
for y in s:
    if abs(y)%100==30:
        t.append(y)
a=max(t)
for i in range(len(s)-2):
    k=0
    if 1000<=s[i]<=9999:
        k+=1
    if 1000<=s[i+1]<=9999:
        k+=1
    if 1000<=s[i+2]<=9999:
        k+=1
    if k==0:
        if (s[i]+s[i+1]+s[i+2])>a:
            p.append(s[i]+s[i+1]+s[i+2])
print(len(p),max(p))
