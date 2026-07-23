class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftBounds, rightBounds = [None] * n, [None] * n

        #compute leftBounds
        stack = []
        leftBounds[0] = 0
        stack.append((heights[0], leftBounds[0]))
        for i in range(1, n):
            leftBound = i
            while(stack and stack[-1][0] >= heights[i]):
                leftBound = stack.pop()[1]
            leftBounds[i] = leftBound
            stack.append((heights[i], leftBound))

        #compute rightBounds
        stack = []
        rightBounds[n - 1] = n - 1
        stack.append((heights[n - 1], rightBounds[n - 1]))
        for i in range(n - 2, -1, -1):
            rightBound = i
            while(stack and stack[-1][0] >= heights[i]):
                rightBound = stack.pop()[1]
            rightBounds[i] = rightBound
            stack.append((heights[i], rightBound))

        #compute areas
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, (abs(leftBounds[i]-rightBounds[i])+1)*heights[i])      

        return maxArea
        