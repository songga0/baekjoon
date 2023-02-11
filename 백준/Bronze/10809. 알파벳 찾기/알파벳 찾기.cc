#include <stdio.h>
#include <string.h>

int main(){
  char s[100];
  //a97 z122
  scanf("%s",s);
  
  for(int i=97;i<123;i++){
    int cnt=0;
    for(int j=0;j<strlen(s);j++){
    if(i==(int)s[j]){
      cnt++;
      if(cnt==1){
        printf("%d ",j);
        }
      }
    }
    if(cnt==0)
      printf("-1 ");
  }
}