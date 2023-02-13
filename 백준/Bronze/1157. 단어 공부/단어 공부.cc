#include<stdio.h>
#include<string.h>

int main(){
  char s[1000000];
  scanf("%s",s);
  int size=strlen(s);

  int arr[26];
  for(int i=0;i<size;i++){
    if(s[i]>=97){
      s[i]=s[i]-97;
    }
    else if(s[i]>=65&&s[i]<97){
      s[i]=s[i]-65;
    }
    arr[s[i]]++;
  }
  int max=0,alp;
  for(int i=0;i<26;i++){
    if(max<arr[i]){
      max=arr[i];
      alp=i+65;
    }
  }
  int br=0;
  for(int i=0;i<26;i++){
    if(max==arr[i]){
      br++;
    }
  }
  if(br>1){
    printf("?");
  }
  else{
    printf("%c",alp);
  }
  
}