#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int min(int a, int b) {
    return (a < b) ? a : b;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    int *arr = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int *dp = (int *)malloc(n * sizeof(int));
    dp[0] = 0; 
    dp[1] = abs(arr[1] - arr[0]); 

 
    for (int i = 2; i < n; i++) {
        int option1 = dp[i-1] + abs(arr[i] - arr[i-1]); 
        int option2 = dp[i-2] + abs(arr[i] - arr[i-2]); 
        dp[i] = min(option1, option2);
    }

    printf("%d\n", dp[n-1]);

    free(arr);
    free(dp);
    return 0;
}
