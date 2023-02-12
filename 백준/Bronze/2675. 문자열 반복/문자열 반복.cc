#include <stdio.h>
#include <string.h>

int main(){
  int t;
  scanf("%d",&t);
  for(int i=0;i<t;i++){
    int r;
    char arr[1000];
    scanf("%d %s",&r,arr);
    for(int j=0;j<strlen(arr);j++){
      for(int k=0;k<r;k++){
        printf("%c",arr[j]);
      }
    }
    printf("\n");
  }
}