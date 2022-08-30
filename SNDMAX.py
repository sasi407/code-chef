for i in range(int(input())):
    x,y,z=map(int,input().split())
    a=[x,y,z]
    a.sort()
    a.pop(-1)
    b=a[-1]
    print(b)