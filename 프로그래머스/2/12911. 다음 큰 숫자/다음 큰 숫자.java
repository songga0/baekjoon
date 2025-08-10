class Solution {
    public int solution(int n) {
        int answer = n;
        String b1 = Integer.toBinaryString(n);
        int b1cnt = 0;
        for (int i = 0; i < b1.length(); i++) {
            if (b1.charAt(i) == '1') {
                b1cnt++;
            }
        }

        while (true) {
            answer++;
            String b2 = Integer.toBinaryString(answer);
            int b2cnt = 0;
            for (int j = 0; j < b2.length(); j++) {  // j < b2.length()
                if (b2.charAt(j) == '1') {
                    b2cnt++;
                }
            }
            if (b1cnt == b2cnt) {
                break;
            }
        }
        return answer;
    }
}
