class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        fcity = [i for i,j in costs]
        Diff = [j - i for i,j in costs]
        return sum(fcity) + sum(sorted(Diff)[:len(costs)//2])
        
