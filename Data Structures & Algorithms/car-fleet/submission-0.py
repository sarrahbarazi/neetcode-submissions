class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its calculated time to reach the target
        pairs = [[p, (target - p) / s] for p, s in zip(position, speed)]
        
        # Sort cars based on their starting position in descending order (closest to target first)
        pairs.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        
        for p, t in pairs:
            stack.append(t)
            # If there are at least two fleets in the stack, check if the car behind
            # reaches the target faster than or at the same time as the fleet ahead.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # It catches up and becomes part of the ahead car's fleet, so remove its time
                stack.pop()
                
        # The number of remaining elements in the stack is the number of distinct fleets
        return len(stack)