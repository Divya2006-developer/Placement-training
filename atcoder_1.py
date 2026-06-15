def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a

N,A,B,C,D=map(int,input().split())
total=0
total+=gcd(A+B,C+D)
for i in range(1,N):
  total+=gcd(A+B+i,C+D+(i*4))
ans=total%998244353
print(ans)
