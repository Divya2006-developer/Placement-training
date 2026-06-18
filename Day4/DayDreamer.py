import sys

def solve():
    s = sys.stdin.read().strip()
    words = ["dream", "dreamer", "erase", "eraser"]
    possible = True
    while len(s) > 0:
        matched = False
        for w in words:
            if s.endswith(w):
                s = s[:-len(w)]
                matched = True
                break  
        
        if not matched:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
