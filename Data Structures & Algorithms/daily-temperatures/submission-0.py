class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            daysStack = []
            
            # Push future elements onto our tracking stack
            for j in range(i + 1, len(temperatures)):
                daysStack.append(temperatures[j])
                # If we hit a strictly warmer day, we stop pushing
                if temperatures[j] > current_temp:
                    break
            else:
                # If the loop finished without breaking, no warmer day was found.
                # We empty the stack so its length becomes 0.
                while daysStack:
                    daysStack.pop()
            
            result.append(len(daysStack))
            
        return result