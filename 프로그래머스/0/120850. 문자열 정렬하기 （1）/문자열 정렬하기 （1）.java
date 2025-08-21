import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(String my_string) {
        int[] answer = {};
        ArrayList<Integer> list=new ArrayList<>();
        for (int i=0;i<my_string.length();i++){
            if(Character.isDigit(my_string.charAt(i))){
                list.add(my_string.charAt(i) - '0');
            }
        }
        answer=new int[list.size()];
        for(int j=0;j<list.size();j++){
            answer[j]=list.get(j);
        }
        Arrays.sort(answer);
        return answer;
    }
}