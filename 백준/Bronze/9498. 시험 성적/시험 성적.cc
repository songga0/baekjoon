#include <stdio.h>

int main(){
    int s;
    scanf("%d",&s);
    if(s>=90&&s<=100){
        printf("A");
    }
    else if(s>=80&&s<90){
        printf("B");
    }
    else if(s>=70&&s<80){
        printf("C");
    }
    else if(s>=60&&s<70){
        printf("D");
    }
    else{
        printf("F");
    }
}