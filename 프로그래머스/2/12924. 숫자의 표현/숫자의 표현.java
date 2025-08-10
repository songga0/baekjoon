class Solution {
    public int solution(int n) {
        int answer = 0;
        //홀수일때는 나눠떨어져야함 짝수일때는 짝수의 반값만큼 남아야됨
        int i=1;
        while(i*(i+1)/2 <= n){
            if(i%2!=0){//홀수일 경우
                if(n%i==0){
                    answer+=1;
                }
            }
            else{
                int j=i/2;
                if(n%i==j){
                    answer+=1;
                }
            }
            i++;
        }
        return answer;
    }
}