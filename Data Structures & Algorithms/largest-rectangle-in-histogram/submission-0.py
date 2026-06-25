class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Pairs of (index, height)
        
        for i, h in enumerate(heights):
            start = i
            # Maintain a monotonically increasing stack
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                # Calculate area with the popped height
                max_area = max(max_area, height * (i - idx))
                # The current bar can extend backward to the index of the popped bar
                start = idx
            
            stack.append((start, h))
            
        # Clear out any remaining bars in the stack
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
            
        return max_area
        