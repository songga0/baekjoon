import java.util.ArrayList;

class Solution {
    public int[] solution(String[] strlist) {
        int[] answer = new int[strlist.length];
        ArrayList<Integer>list=new ArrayList<>();
        for (int i=0;i<strlist.length;i++){
            list.add(strlist[i].length());
        }
        for (int j=0;j<strlist.length;j++){
            answer[j]=list.get(j);
        }
        return answer;
    }
}