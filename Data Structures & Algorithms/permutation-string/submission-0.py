class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        #frequency arrays
        s1_count, s2_count = [0]*26, [0]*26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # 1. Initialize our matches counter (out of 26 possible lowercase English letters)
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # 2. Set up our left pointer and start sliding the window to the right
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            # Add the incoming character from the right (r)
            r_idx = ord(s2[r]) - ord('a')
            s2_count[r_idx] += 1
            if s1_count[r_idx] == s2_count[r_idx]:
                matches += 1
            elif s1_count[r_idx] + 1 == s2_count[r_idx]:
                matches -= 1
                
            # Remove the outgoing character from the left (l)
            l_idx = ord(s2[l]) - ord('a')
            s2_count[l_idx] -= 1
            if s1_count[l_idx] == s2_count[l_idx]:
                matches += 1
            elif s1_count[l_idx] - 1 == s2_count[l_idx]:
                matches -= 1
                
            l += 1 # Slide the left boundary forward
            
        return matches == 26