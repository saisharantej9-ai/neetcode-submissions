

class Solution {
    public boolean hasDuplicate(int[] nums) {
        // 1. Sort the array so duplicates sit next to each other
        Arrays.sort(nums);
        
        // 2. Loop through and compare each element to its NEXT neighbor
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return true; // Found a duplicate!
            }
        }
        
        // 3. If the loop finishes without finding anything
        return false; 
    }
}
