#include<stdio.h>

int main(){
    int h,m;
    scanf("%d %d",&h,&m);
    int c;
    scanf("%d",&c);
    m=m+c;
    if(m>=60){
      while(m>=60){
        m=m-60;
        h=h+1;
      }
    }
    if(h>=24){
        while(h>=24){
            h=h-24;
        }
    }
    printf("%d %d",h,m);
}