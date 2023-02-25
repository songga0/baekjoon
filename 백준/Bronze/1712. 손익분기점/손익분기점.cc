#include<stdio.h>

int main(){
  int a,b,c;
  scanf("%d %d %d",&a,&b,&c);
  int res;
  if(b>=c){
    printf("-1\n");
  }
  else{
    res=(a/(c-b))+1;
    printf("%d\n",res);
  }
}