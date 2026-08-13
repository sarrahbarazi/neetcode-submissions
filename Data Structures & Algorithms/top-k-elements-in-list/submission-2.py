class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0)+ 1

        pairs = []
        for key, value in freqMap.items():
            pairs.append([value, key])
        pairs.sort(reverse=True)
        return [pairs[1] for pairs in pairs[:k]]





        




        