#include<stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
  int tmp;
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if(arr[i]>arr[j]){
              tmp=arr[i];
              arr[i]=arr[j];
              arr[j]=tmp;
            }
        }
    }
  for(int i=0;i<n;i++){
    printf("%d\n",arr[i]);
  }
}