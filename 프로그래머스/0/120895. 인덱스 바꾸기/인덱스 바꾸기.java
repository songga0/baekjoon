class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        for(int i=0;i<num1;i++){
            answer+=my_string.charAt(i);
        }
        answer+=my_string.charAt(num2);
        for(int j=num1+1;j<num2;j++){
            answer+=my_string.charAt(j);
        }
        answer+=my_string.charAt(num1);
        for(int k=num2+1;k<my_string.length();k++){
            answer+=my_string.charAt(k);
        }
        return answer;
    }
}