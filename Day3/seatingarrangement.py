def func:
    t=int(input())
    while t>0:
        f,t,s=map(int,input().split())
        s=input()
        count=0
        out=[]
        free = [[0 for _ in range(s)] for _ in range(t)]

        for i in s:
            if i!='A' and i!='I' i!='E':
                print("The friends should either I/A/E")
            if i=='E':
                for i in free:
                    if i==1:
                        
                out.append(i)
            elif i==''
