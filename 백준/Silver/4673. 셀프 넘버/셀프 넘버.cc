#include<stdio.h>

int main(){
  int arr[10001];
  int sum=0;
  for(int i=1;i<10001;i++){
    int n=i;
    sum=n;
    while(n>0){
      sum=sum+(n%10);
      n=n/10;
    }
    if(sum<10001){
      arr[sum]=1;
    }
  }
  for(int i=1;i<10001;i++){
    if(arr[i]!=1){
      printf("%d\n",i);
    }
  }
}