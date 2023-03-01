#include<stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    for(int k=1;k<=n;k++){
        for(int i=k;i<n;i++){
            printf(" ");
        }
        for(int j=2*k-1;j>0;j--){
            printf("*");
        }
        printf("\n");
    }
}