#include <stdio.h>

int main(){
  int n;
  int arr[1000];
  int a,b,c,d,e;
  int cnt=0;
  scanf("%d",&n);
  if(n<100){
    for(int i=1;i<=n;i++){
      cnt++;
    }
  }
  else{
    for(int i=1;i<100;i++){
      cnt++;
    }
    for(int i=100;i<=n;i++){
      a=i/100;//100의 자리수
      b=(i%100)/10;
      c=i%10;
      d=b-a;
      e=c-b;
      if(d==e){
        cnt++;
      }
    }
  }
  printf("%d\n",cnt);
}