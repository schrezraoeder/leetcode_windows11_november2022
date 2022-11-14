
// this answer is just intended as a semantic-translation, as close to line-by-line 
// but concept-by-concept by necessity as C++ & Python are sufficiently far apart to
// often necessitate that, from my python solution. A major goal for now is just to 
// keep the C++ code very simple and as conceptually similar to my python solution as I'm **rusty** in C++. 
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int ix = 0; 
        int jx = 1;
        if (nums.size() == 2) {
            return (nums[ix] - 1) * (nums[jx] - 1); 
        }
        vector<int> max_two = {0, 1}; 
        max_two[0] = max(nums[ix], nums[jx]); 
        max_two[1] = min(nums[ix], nums[jx]); 
        int number = -1; 
        int max_so_far = max_two[0]; 
        for (int i = 2; i < nums.size(); i++) {
            number = nums[i]; 
            if (number >= max_so_far) {
                max_two[1] = max_so_far; 
                max_two[0] = number; 
                max_so_far = number; 
            }
            else if (number >= max_two[1]) {
                max_two[1] = number; 
            }
        }
        return (max_two[0] - 1) * (max_two[1] - 1); 
        
        
    }
};