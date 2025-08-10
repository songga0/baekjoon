class Solution {
    public String solution(String s) {
        String[] words = s.split(" ", -1); // 빈 문자열도 포함
        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < words.length; i++) {
            String word = words[i];

            if (word.length() > 0) {
                char first = word.charAt(0);
                if (Character.isLetter(first)) {
                    // 첫 글자 대문자 + 나머지 소문자
                    answer.append(Character.toUpperCase(first));
                    answer.append(word.substring(1).toLowerCase());
                } else {
                    // 첫 글자 알파벳 아니면 단어 전체 소문자
                    answer.append(word.toLowerCase());
                }
            }
            // 빈 단어일 경우 그대로 (공백 유지 목적)
            
            if (i != words.length - 1) {
                answer.append(" ");
            }
        }
        return answer.toString();
    }
}
