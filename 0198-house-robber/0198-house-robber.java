
class Solution {
    
    Map<Integer, Integer> cache = new HashMap<Integer,Integer>();
    public int rob(int[] nums) {

      int zeroHouseSum = robberHelper(0, nums);
      int firstHouseSum =  robberHelper(1, nums);

      return Math.max(zeroHouseSum, firstHouseSum);

    }

    private int robberHelper(int index, int[] nums){
      if(index >= nums.length){
        return 0;        
      }
        if(cache.containsKey(index)){
            return cache.get(index);
        }
        
      int secondHouseSum = nums[index] + robberHelper(index+2, nums);
      int thirdHouseSum = nums[index] + robberHelper(index+3, nums);

       int max = Math.max(secondHouseSum, thirdHouseSum);
        cache.put(index, max);
        
        return max;
      
    }
 
}