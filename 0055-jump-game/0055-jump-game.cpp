// Note: i looked at the neetcode solution first, 
// translating my python code to C++ 
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goal = nums.size() - 1; 
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (i + nums[i] >= goal) {
                goal = i; 
            }
        }
        return (goal == 0); 
        
    }
};

