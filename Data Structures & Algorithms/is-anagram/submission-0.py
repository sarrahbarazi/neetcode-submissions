class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        frequencyMap_s={}
        frequencyMap_t={}

        for char in s:
            if char in frequencyMap_s:
                frequencyMap_s[char]+=1
            else:
                frequencyMap_s[char]= 1

        for char in t:
            if char in frequencyMap_t:
                frequencyMap_t[char]+=1
            else:
                frequencyMap_t[char]=1
        
        if frequencyMap_t == frequencyMap_s:
            return True
        else:
            return False


        

            
        