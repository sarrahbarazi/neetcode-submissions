class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # Ensure A is the smaller array so binary search is faster O(log(min(m, n)))
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # Partition index for A
            j = half - i - 2  # Partition index for B
            
            # Handle edge cases where partitions are empty using infinity boundaries
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Check if partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # If total number of elements is odd
                if total % 2:
                    return min(Aright, Bright)
                # If total number of elements is even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            elif Aleft > Bright:
                r = i - 1  # Too many elements from A in the left partition, move left
            else:
                l = i + 1  # Too few elements from A in the left partition, move right