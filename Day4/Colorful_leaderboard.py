import sys
n=int(input())
line=sys.stdin.read()
l=line.split()
l=[int(x) for x in l]
a=[0,0,0,0,0,0,0,0]
count1=0
count2=0
for i in l:
  if i>=0 and i<=399:
    a[0]=1
  elif i>=400 and i<=799:
    a[1]=1
  elif i>=800 and i<=1199:
    a[2]=1
  elif i>=1200 and i<=1599:
    a[3]=1
  elif i>=1600 and i<=1999:
    a[4]=1
  elif i>=2000 and i<=2399:
    a[5]=1
  elif i>=2400 and i<=2799:
    a[6]=1
  elif i>=2800 and i<=3199:
    a[7]=1
  elif i>=3200:
    count2=count2+1
    
count1+=a.count(1)
count2+=a.count(1)
if count1==0:
  count1=1
    
print(count1,count2)
    
