class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #group numbers by frequency
        #if number is seen +1 if not add to hash map
        # {1: 1, 2: 2, 3: 3}
        # sort the hashmap by descending order
        # display for k items in dictionary

        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1

        desc_list = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        
        j=0
        output = []
        for num, count in desc_list:
            if j<k:
                output.append(num)
                j+=1
        return output

    
    

        