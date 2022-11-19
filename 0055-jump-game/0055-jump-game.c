// Note: I looked at the neetcode solution first, 
// translating my python->c++->java code to C 
bool canJump(int* nums, int numsSize){
    int goal = numsSize - 1; 
    for (int i = goal; i >= 0; i--) {
        if (i + nums[i] >= goal) {
            goal = i; 
        }
    }
    return (goal == 0); 

}


