class Solution:
    #[2,4,3,5,0] -> 1
    #[3,4,2,5,0] swap 3,2
    #[5,4,2,3,0] skip 5, swap 4,0
    #[5,0,2,3,4] swap 5,0
    #[0,5,2,3,4]
    #missing number is 1 as 1 isn't at nums[1]

    #[1,0] -> 2
    #[0,1] swap 1,0
    #missing number is 2 since every element is in the right place
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        #go through each index and continue swapping until each element is in the right place (where the value at the index is the same as the index)
        for i in range(n):
            #while current number not in the right position and number isn't the max number
            while not nums[i] == i and not nums[i] == n:
                swap = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = swap

        #find which one is missing
        #after each number is swapped to the right position only the maximum number (n) has been ignored and in the spot where the missing number is
        for i, num in enumerate(nums):
            if not i == num:
                return i

        #if every element is in the right position then missing number is the maximum number
        return n
