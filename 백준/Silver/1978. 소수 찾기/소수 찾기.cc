#include<stdio.h>

int main(){
    int N;
    scanf("%d",&N);
    int num;
    int cnt=0;
    for(int i=0;i<N;i++){
        scanf("%d",&num);
        if(num==1){
          continue;
        }
        else if(num==2){
          cnt++;
        }
        else{
          for(int j=2;j<num;j++){
              if(num%j==0){
              break;
              }
              if(j==num-1){
                 cnt++;
              }
          }
         }
    }
    printf("%d\n",cnt);
    return 0;
}