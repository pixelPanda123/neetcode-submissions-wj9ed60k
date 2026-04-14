class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        slots = []
        fleets = 1 
        for x,y in zip(position, speed):
            slots.append((x,y))
        slots.sort(reverse=True)
        stack = []
        for p,s in slots: 
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)
        

