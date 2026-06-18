import sys

def main():

    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    a = [int(x) for x in data[2:2+n]]
    a.sort()

    ops = []
    idx = 2 + n
    for _ in range(m):
        b = int(data[idx])
        c = int(data[idx+1])
        ops.append((c, b))
        idx += 2

    ops.sort(key=lambda x: x[0], reverse=True)
    
    card_idx = 0
    for val, count in ops:
        # Replace elements if the pool value is strictly greater
        while card_idx < n and count > 0 and a[card_idx] < val:
            a[card_idx] = val
            card_idx += 1
            count -= 1
            
        if card_idx >= n or a[card_idx] >= val:
            if card_idx >= n:
                break

    print(sum(a))

if __name__ == '__main__':
    main()
