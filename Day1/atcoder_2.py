import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0] * (n + 1)

    for x in a:
        freq[x] += 1

    need = [0] * (n + 1)
    required = 0

    for v in range(1, n + 1):
        if freq[v] > 1:
            need[v] = freq[v] - 1
            required += 1

    # All elements are distinct
    if required == 0:
        print(n)
        continue

    inside = [0] * (n + 1)

    left = 0
    satisfied = 0
    min_len = n

    for right in range(n):
        x = a[right]
        inside[x] += 1

        if need[x] > 0 and inside[x] == need[x]:
            satisfied += 1

        while satisfied == required:
            min_len = min(min_len, right - left + 1)

            y = a[left]

            if need[y] > 0 and inside[y] == need[y]:
                satisfied -= 1

            inside[y] -= 1
            left += 1

    print(n - min_len)
