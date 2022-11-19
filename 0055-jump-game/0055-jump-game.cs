// Note: i looked at the neetcode.io video first 
// translating my python->c++->java->c->javascript code to C# 
// unlike the others i've never actually taken a course in C# 
// or used it other than for a few leetcode problems 
public class Solution {
    public bool CanJump(int[] nums) {
        int goal = nums.Length - 1; 
        for (int i = goal; i >= 0; i--) {
            if (i + nums[i] >= goal) {
                goal = i;
            }
        }
        return (goal == 0);         
    }
}

