#include<stdio.h>
int main(){
  int m,n;
  scanf("%d %d",&m,&n);
  int A[m],B[n],c[n];
  int i,j;
  for(i=0;i<m;i++){
    scanf("%d",&A[i]);
  }
  for(j=0;j<n;j++){
    scanf("%d",&B[j]);
  }
  int count=0;
  for(i=0;i<m;i++){
    for(j=0;j<n;j++){
      if ((A[i]*2<= B[j]) && (B[j]!=0)){
        count++;
        B[j]=0;
        break;
      }
  }
  }
  printf("%d",count);
  }
