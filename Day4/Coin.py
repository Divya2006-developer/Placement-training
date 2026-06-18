import sys

def main():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    p = [float(x) for x in data[1:]]

    # dp[j] represents the probability of having exactly j heads
    dp = [0.0] * (n + 1)
    dp[0] = 1.0  # Base case

    for i in range(n):
        current_p = p[i]
        # Update dp array backwards to prevent overwriting values needed for the same step
        for j in range(i + 1, -1, -1):
            head_prob = dp[j - 1] * current_p if j > 0 else 0.0
            tail_prob = dp[j] * (1.0 - current_p)
            dp[j] = head_prob + tail_prob

    # Sum all cases where the number of heads is strictly greater than tails
    ans = sum(dp[j] for j in range(n // 2 + 1, n + 1))
    
    print(f"{ans:.10f}")

if __name__ == '__main__':
    main()
