class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for num in nums:
            numbers[num] = 1 + numbers.get(num, 0)
        
        for num in numbers:
            if numbers.get(target-num) is not None and (target-num is not num or numbers.get(target-num) > 1):
                index1 = nums.index(num)
                if(num == target-num):
                    index2 = nums.index(target-num, index1+1)
                else:
                    index2 = nums.index(target-num)
                return [min(index1, index2), max(index1, index2)]
        