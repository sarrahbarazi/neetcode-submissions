class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]]=i

        max_length = 1

        for i in range(len(nums)):
            current_num = nums[i]
            if (current_num - 1) not in hashmap:
                current_chain_len = 1
                while (current_num + 1) in hashmap:
                    current_chain_len +=1
                    current_num += 1
                max_length = max(max_length, current_chain_len)

        return max_length 
        