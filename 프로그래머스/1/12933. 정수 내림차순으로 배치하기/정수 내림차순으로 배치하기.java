import java.util.Arrays;
class Solution {
    public long solution(long n) {
        long answer = 0;
        int l=Long.toString(n).length();//길이
        int[] x = new int[l];
        for (int i=0;i<l;i++){
            x[i]=(int)(n%10);
            n/=10;
        }
        Arrays.sort(x);
        for(int j=0;j<l;j++){
            answer*=10;
            answer+=x[l-j-1];
        }
        return answer;
    }
}