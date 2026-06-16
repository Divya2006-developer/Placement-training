import sys

def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    sushi = [int(x) for x in input_data[1:]]

    c1 = sushi.count(1)
    c2 = sushi.count(2)
    c3 = sushi.count(3)

    dp = [[[0.0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

    for k in range(N + 1):         
        for j in range(N + 1):      
            for i in range(N + 1): 
                
                total = i + j + k
                if total == 0 or total > N:
                    continue
                

                val = N
                if i > 0: val += i * dp[k][j][i-1]
                if j > 0: val += j * dp[k][j-1][i+1]
                if k > 0: val += k * dp[k-1][j+1][i]
                
                dp[k][j][i] = val / total

    print(f"{dp[c3][c2][c1]:.14f}")

if __name__ == "__main__":
    solve()
