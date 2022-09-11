for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a>b:
        if a>c:
            print("ALICE")
        else:
            print("CHARLIE")
    else:
        if b>c:
            print("BOB")
        else:print("CHARLIE")