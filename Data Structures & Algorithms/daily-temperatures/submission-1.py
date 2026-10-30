class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0] * n
        monotonic_stack = [] #decreasing

        for i, temperature in enumerate(temperatures):
            while(monotonic_stack and monotonic_stack[-1][1] < temperature):
                top_index = monotonic_stack.pop()[0]
                out[top_index] = (i - top_index)
            monotonic_stack.append((i, temperature))

        return out