class Solution:
    def twoCitySchedCost(self, costs) -> int:
        self.sortHelper(costs)
        
        cnt_A = 0
        cnt_B = 0
        costs_len = len(costs)
        sum_ = 0
        
        for i in range(costs_len):
            if costs[i][0] < costs[i][1]:
                if cnt_A < costs_len // 2:
                    cnt_A += 1
                    sum_ += costs[i][0]
                else:
                    cnt_B += 1
                    sum_ += costs[i][1]
            else:
                if cnt_B < costs_len // 2:
                    cnt_B += 1
                    sum_ += costs[i][1]
                else:
                    cnt_A += 1
                    sum_ += costs[i][0]
        return sum_
        
    
    def sortHelper(self, costs):
        # sort by absolute difference
        tmp_abs_bucket = [abs(costs[i][0] - costs[i][1]) for i in range(len(costs))]
        for i in range(len(tmp_abs_bucket) - 1):
            max_ = i
            for j in range(i + 1, len(tmp_abs_bucket)):
                if tmp_abs_bucket[max_] < tmp_abs_bucket[j]: max_ = j
            tmp_abs_bucket[max_], tmp_abs_bucket[i] = tmp_abs_bucket[i], tmp_abs_bucket[max_]       
            costs[max_], costs[i] = costs[i], costs[max_]       # the list that really needs to be sorted is costs
        # print(tmp_abs_bucket)
        
# a = Solution()
# print(a.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
