#include<stdio.h>

int main(){
  int a,b,c;
  scanf("%d %d %d",&a,&b,&c);
  if(a==b&&b==c){
    printf("%d",10000+(a*1000));
  }
  if(a==b){
    if(b!=c){
      printf("%d",1000+(b*100));
    }
  }
  if(a==c){
    if(b!=c){
      printf("%d",1000+(a*100));
    }
  }
  if(b==c){
    if(a!=c){
      printf("%d",1000+(b*100));
    }
  }
  if(a!=b&&b!=c&&a!=c){
    if(a>b){
      if(b>c){
        printf("%d",a*100);
      }
      else{
        if(a>c){
          printf("%d",a*100);
        }
        else{
          printf("%d",c*100);
        }
      }
    }
    else{//b>=a
      if(a>c){
        printf("%d",b*100);
      }
      else{//c>=a
        if(b>c){
          printf("%d",b*100);
        }
        else{
          printf("%d",c*100);
        }
      }
    }
  }
}