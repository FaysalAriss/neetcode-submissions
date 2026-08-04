class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        top = []
        for _ in range(k):
            maxNum = nums[0]
            maxCount = 0
            for num, count in counts.items():
                if count > maxCount:
                    maxCount = count
                    maxNum = num
            top.append(maxNum)
            counts.pop(maxNum)
        
        return top