s,e=map(int,input().split())
val=0
for i in range(s,e+1):
  val=val^i
  
print(val)
