for i in range (int(input())):
    a,b,c=map(int,(input().split()))
    if (a+b)/2<35 or (b+c)/2<35 or (c+a)/2<35:
        print("fail")
    else:
        print("pass")