array=[]
result=0
try:
  size=int(input())
  array=list(map(int,input().split()))
  if len(array)==size:
    for i in array:
      result=result|i
    print(result)
  else:
    raise IndexError
except IndexError:
  pass
except ValueError:
  pass
