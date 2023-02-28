#include<stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    
    for(int i=0;i<n;i++){
        for(int j=n-i;j<n;j++){
            printf(" ");
        }
        for(int k=i;k<n;k++){
            printf("*");
        }
        printf("\n");
    }
}