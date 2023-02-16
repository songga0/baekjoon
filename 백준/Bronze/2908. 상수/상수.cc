#include<stdio.h>
#include<string.h>

int main(){
  int a,b;
  int n,x=0,y=0;
  scanf("%d %d",&a, &b);
  n=100;
  while(a>0){
    x=x+((a%10)*n);
    a=a/10;
    n=n/10;
  }
  n=100;
  while(b>0){
    y=y+((b%10)*n);
    b=b/10;
    n=n/10;
  }
  if(x>y){
  printf("%d",x);
}
else{
  printf("%d",y);
}
}