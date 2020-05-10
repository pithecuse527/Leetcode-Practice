#!/usr/bin/python3

class Solution:
    def findJudge(self, N: int, trust) -> int:
        # base caes that does not need the iteration
        if N == 0:
            return -1
        if N == 1:
            return 1
        
        # tuple is element
        # first val of tuple is the number of input
        # second val of tuple is the number of output
        # incides indicate each person's number
        graph_input_output = [[0,0]]       # 0'th index will not be used
        
        for i in range(1, N+1):
            graph_input_output.append([0,0])

        for i in range(len(trust)):
            person_from = trust[i][0]
            person_to = trust[i][1]
            graph_input_output[person_to][0] += 1         # increase input
            graph_input_output[person_from][1] += 1       # increase output
            
        
        for i in range(1, len(graph_input_output)):
            if graph_input_output[i][0] == N-1 and graph_input_output[i][1] == 0:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
