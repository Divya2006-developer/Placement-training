#include <stdio.h>
#include<stdlib.h>
int main()
{
    int m,n,x;
    int **mat;
    scanf("%d %d",&m,&n);
    mat=(int **)malloc(n*sizeof(int *));
    int i,j;
    for(i=0;i<n;i++){
       mat[i]=(int *)malloc(m*sizeof(int));
    }
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            scanf("%d",&mat[i][j]);
        }
    }
    int f=0;
    scanf("%d",&x);
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            if(mat[i][j]==x){
                f=1;
            }
        }
    }
    if(f){
        printf("1");
    }
    else{
        printf("0");
    }
    
}
