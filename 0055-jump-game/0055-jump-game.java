// Note I looked at the neetcode solution first,
// translating my python->c++ code to java 
class Solution {
    public boolean canJump(int[] nums) {
        int goal = nums.length - 1; 
        for (int i = goal; i >= 0; i--) {
            if (i + nums[i] >= goal) {
                goal = i;
            }
        }
        return (goal == 0); 
        
    }
}
