class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2
            
            # If found, return the index
            if nums[mid] == target:
                return mid
            # If target is smaller, look in the left half
            elif target < nums[mid]:
                high = mid - 1
            # If target is larger, look in the right half
            else:
                low = mid + 1
                
        # Target was not found in the array
        return -1