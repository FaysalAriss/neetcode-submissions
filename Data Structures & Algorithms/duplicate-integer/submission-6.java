class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numbers = new HashSet<>();
        int i = 0;
        while(i < nums.length && numbers.add(nums[i])){
            i++;
        }
        return i != nums.length;
    }
}