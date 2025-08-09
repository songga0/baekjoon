class Solution {
    public String solution(String s) {
        int l=s.length();
        String answer = "";
        int x=0;
        if(l%2==0){
            x=l/2-1;
            answer+=s.charAt(x);
            answer+=s.charAt(x+1);
        }
        else{
            x=(int)(l/2);
            answer+=s.charAt(x);
        }
        return answer;
    }
}