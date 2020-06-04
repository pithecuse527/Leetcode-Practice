class Solution:
    def twoCitySchedCost(self, costs) -> int:
        len_half = len(costs) // 2
        
        sorted_by_A = self.sortHelper(costs, 0)  # sorted by city A
        first_sum = 0
        for i in range(len_half):
            first_sum += costs[i][0]
            first_sum += costs[i+len_half][1]
        
        sorted_by_B = self.sortHelper(costs, 1)  # sorted by city B
        second_sum = 0
        for i in range(len_half):
            second_sum += costs[i][1]
            second_sum += costs[i+len_half][0]
            
        return min(first_sum, second_sum)
        
    
    def sortHelper(self, costs, city):
        for i in range(len(costs)):
            min_idx = i
            for j in range(i+1, len(costs)):
                if costs[min_idx][city] > costs[j][city]: min_idx = j
            costs[i], costs[min_idx] = costs[min_idx], costs[i]
        return costs
        
a = Solution()
a.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
