#include<stdio.h>

int main(){
    int a,b,c,d,e;
    scanf("%d",&a);
    scanf("%d",&b);
    e=b-(10*(b/10));
    printf("%d\n",a*e);
    d=(b-(100*(b/100))-e)/10;
    printf("%d\n",a*d);
    c=b/100;
    printf("%d\n",a*c);
    printf("%d",(a*e)+(10*(a*d))+(100*(a*c)));
}