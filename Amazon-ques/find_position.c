#include <stdio.h>
#include<stdlib.h>
int main()
{
    int m,n,x;
    int *mat;
    scanf("%d",&n);
    mat=(int *)malloc(n*sizeof(int));
    int i,j;
    for(i=0;i<n;i++){
            scanf("%d",&mat[i]);
    }
    int index=-1;;
    scanf("%d",&x);
    for(i=0;i<n;i++){
            if(mat[i]==x){
                index=i;
            }
        }
    printf("%d",index);
    
}
