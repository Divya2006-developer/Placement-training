def func():
    n=int(input())
    length=len(str(n))
    if length<4:
        print(f"{n} is not a valid car number\n")
        return
    s=0
    while n>0:
        d=n%10
        s+=d
        n=n//10
    if s%3==0 or s%5==0 or s%7==0:
        print("Lucky Number\n")
    else:
        print("Sorry its not my lucky number\n")

func()
