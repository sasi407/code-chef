n=int(input())
s=0
for i in range(1,n+1):
    for j in  range(1,n+1):
        a=i+j
        if a%2!=0:
            s+=1
print(s//2)
