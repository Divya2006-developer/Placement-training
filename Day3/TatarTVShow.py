import sys

def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
  
    t = int(next(iterator))
    
    out = []
    for _ in range(t):
        n = int(next(iterator))
        k = int(next(iterator))
        s = next(iterator)
        

        group_counts = [0] * k
 
        for i in range(n):
            if s[i] == '1':
                group_counts[i % k] += 1
                

        possible = True
        for count in group_counts:
            if count % 2 != 0:
                possible = False
                break
        
        if possible:
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()
