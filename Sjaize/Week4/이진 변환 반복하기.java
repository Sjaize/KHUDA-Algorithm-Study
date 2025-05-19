class Solution {
    public int[] solution(String s) {
        int loop = 0;
        int removed = 0;
        while (!s.equals("1")) {
            StringBuilder sb = new StringBuilder();
            for (char c : s.toCharArray()) {
                if (c == '0') ++removed;
                else sb.append(c);
            }
            s = Integer.toString(sb.length(), 2);
            ++loop;
        }
        return new int[] {loop, removed};
    }
}
