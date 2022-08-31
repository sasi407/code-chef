#to cheack he is eligible or not
for i in range(int(input())):
    x,y,a=map(int,input().split())
    if a>=x and a<y:
        print("yes")
    else:print("no")