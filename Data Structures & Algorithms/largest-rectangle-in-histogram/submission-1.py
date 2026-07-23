class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        bounds = [0] * n

        #compute left bounds
        stack = []
        for i in range(0, n):
            leftBound = i
            while(stack and stack[-1][0] >= heights[i]):
                leftBound = stack.pop()[1]
            bounds[i] = leftBound
            stack.append((heights[i], leftBound))

        #compute right bounds
        stack = []
        for i in range(n - 1, -1, -1):
            rightBound = i
            while(stack and stack[-1][0] >= heights[i]):
                rightBound = stack.pop()[1]
            bounds[i] = abs(bounds[i] - rightBound)
            stack.append((heights[i], rightBound))

        #compute areas
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, (bounds[i]+1)*heights[i])      

        return maxArea
        