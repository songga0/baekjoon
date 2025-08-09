import java.util.Arrays;
import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        int l=arr.length;
        ArrayList<Integer>list=new ArrayList<>();
        for(int i=0;i<l;i++){
            if(arr[i]%divisor==0){
                list.add(arr[i]);
            }
        }
        int []answer;
        if(list.size()==0){
            answer=new int[]{-1};
        }
        else{
            answer=new int[list.size()];
            for(int j=0;j<list.size();j++){
                answer[j]=list.get(j);
            }
        }
        Arrays.sort(answer);
        return answer;
    }
}