import sys

def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
  
    dp = [0, 0, 0]
    
    idx = 1
    for _ in range(n):

        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        

        new_a = a + max(dp[1], dp[2]) 
        new_b = b + max(dp[0], dp[2]) 
        new_c = c + max(dp[0], dp[1]) 

        dp = [new_a, new_b, new_c]
        

    print(max(dp))

if __name__ == '__main__':
    solve()
