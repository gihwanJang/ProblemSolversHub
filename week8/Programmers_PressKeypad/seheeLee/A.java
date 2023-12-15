class Solution {
    static class Node {
        int r;
        int c;
        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    static Node right;
    static Node left;
    static boolean isRight;
    
    static String answer;
    public String solution(int[] numbers, String hand) {
        right = new Node(3, 2);
        left = new Node(3, 0);

        answer = "";
        if(hand.equals("right")) isRight = true;
        else if(hand.equals("left")) isRight = false;
        
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == 1)
                dfs(new Node(0, 0));
            if (numbers[i] == 2)
                dfs(new Node(0, 1));
            if (numbers[i] == 3)
                dfs(new Node(0, 2));
            if (numbers[i] == 4)
                dfs(new Node(1, 0));
            if (numbers[i] == 5)
                dfs(new Node(1, 1));
            if (numbers[i] == 6)
                dfs(new Node(1, 2));
            if (numbers[i] == 7)
                dfs(new Node(2, 0));
            if (numbers[i] == 8)
                dfs(new Node(2, 1));
            if (numbers[i] == 9)
                dfs(new Node(2, 2));
            if (numbers[i] == 0)
                dfs(new Node(3, 1));
        }        
        return answer;
    }
    
    public void dfs(Node dest) {
        if (isLeftPress(dest, isRight)) {
            answer+="L";
        } else {
            answer+="R";
        }
    }
    
    public boolean isLeftPress(Node des, boolean isRight) {
        if (des.c == 0) {
            left.r = des.r;
            left.c = des.c;
            return true;
        } else if (des.c == 2) {
            right.r = des.r;
            right.c = des.c;
            return false;
        }

        int rightDist = Math.abs(des.r - right.r) + Math.abs(des.c - right.c);
        int leftDist = Math.abs(des.r - left.r) + Math.abs(des.c - left.c);

        if (rightDist > leftDist) {
            left.r = des.r;
            left.c = des.c;
            return true;
        } else if (rightDist < leftDist) {
            right.r = des.r;
            right.c = des.c;
            return false;
        } else {
            if (isRight) {
                right.r = des.r;
                right.c = des.c;
                return false;
            } else {
                left.r = des.r;
                left.c = des.c;
                return true;
            }
        }
    }
    
    
}