class Solution:
    #[2,4,3,5,0] -> 1
    #
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        #while current number not in the right position
        for i in range(n):
            while not nums[i] == i and not nums[i] == n:
                swap = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = swap

        #find which one is missing
        for i, num in enumerate(nums):
            if not i == num:
                return i

        return n
