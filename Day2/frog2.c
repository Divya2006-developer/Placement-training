#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INF 1000000000

int min(int a, int b) {
    return (a < b) ? a : b;
}

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;

    int *arr = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        if (scanf("%d", &arr[i]) != 1) return 0;
    }

    int *dp = (int *)malloc(n * sizeof(int));
    dp[0] = 0; 
    for (int i = 1; i < n; i++) {
        dp[i] = INF;
    }

    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= k; j++) {
            if (i - j >= 0) {
                dp[i] = min(dp[i], dp[i-j] + abs(arr[i] - arr[i-j]));
            }   
        }
    }

    printf("%d\n", dp[n-1]);

    free(arr);
    free(dp);
    return 0;
}
