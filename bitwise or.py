array=[]
result=0
size=int(input())
array=list(map(int,input().split()))
for i in array:
  result=result|i
print(result)
