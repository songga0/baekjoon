#include<stdio.h>
#include<string.h>

int main(){
    char arr[1000000];
    int cnt=1,l;
    scanf("%[^\n]",arr);
    l=strlen(arr);
    if(arr[0]==' ') cnt--;
    if(arr[l-1]==' ') cnt--;
    for(int i=0;i<l;i++){
      if(arr[i]==' '){
        cnt++;
      }
    }
  printf("%d\n",cnt);
  return 0;
}