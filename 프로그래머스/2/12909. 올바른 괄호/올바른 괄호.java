class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int l = s.length();
        int x=0;
        for(int i=0;i<l;i++){
            if(s.charAt(i)=='('){
                x+=1;
            }
            else if(s.charAt(i)==')'){
                x-=1;
            }
            if(x<0){
                answer=false;
                break;
            }
        }
        if(x>0){
            answer=false;
        }
        return answer;
    }
}