class Solution {
    public int reverse(int x) {
        long reversed = 0; 

        while (x != 0) {
            int digit = x % 10;       // Extract last digit
            reversed = reversed * 10 + digit; // Append digit
            x /= 10;                  // Remove last digit

            // Check for overflow beyond int range
            if (reversed > Integer.MAX_VALUE || reversed < Integer.MIN_VALUE) {
                return 0; // Return 0 if overflow occurs
            }
        }

        return (int) reversed; // Safe cast back to int
    }
}
