try:
    a,b=map(int,input().split())
    sum=a+b
    if sum%2==0:
        print("even")
    else:
    	print("odd")
except ValueError:
    pass
