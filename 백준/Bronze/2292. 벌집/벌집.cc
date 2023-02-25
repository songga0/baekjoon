#include<stdio.h>

int main(){
  int n;
  scanf("%d",&n);
  n=n-1;
  int result=1;
  if(n==0){
    printf("1\n");
  }
  else if(n>=1&&n<=6){
    printf("2\n");
  }
  else{
    while(n>0){
      n=n-(result*6);
      result++;
    }
    printf("%d\n",result);
  }
}