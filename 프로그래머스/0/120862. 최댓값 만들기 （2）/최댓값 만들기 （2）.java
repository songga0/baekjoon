import java.util.Arrays;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
        int x= numbers[0]*numbers[1];
        int l=numbers.length;
        int y= numbers[l-1]*numbers[l-2];
        if (x>y){
            answer=x;
        }
        else{
            answer=y;
        }
        return answer;
    }
}