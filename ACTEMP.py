for t in range(int(input())):
    a,b,c=map(int,input().split())
    if b>=a:
        if b>=c:
            print("yes")
        else:print("no")
    else:print("no")