/**
 * @param {number[]} nums
 * @return {boolean}
 */

//Note: i looked at the Neetcode.io solution first.
// i'm just translating my python (/c++/java/c) code to javascript 
var canJump = function(nums) {
    goal = nums.length - 1; 
    for (i = goal; i >= 0; i--){
        if (i + nums[i] >= goal) {
            goal = i; 
        }
    }
    return (goal == 0); 
    
};





