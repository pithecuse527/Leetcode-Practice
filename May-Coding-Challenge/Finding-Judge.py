#!/usr/bin/python3

class Solution:
    def findJudge(self, N: int, trust) -> int:
        # base caes that does not need the iteration
        if N == 0:
            return -1
        if N == 1:
            return 1

        person_input_output = [0 for i in range(N+1)]       # 0'th index will not be used

        # if output happens at least one time, that candidate is not suitable for the Judge
        for i in range(len(trust)):
            person_from = trust[i][0]
            person_to = trust[i][1]
            person_input_output[person_to] += 1           # increase input
            person_input_output[person_from] -= 1       # decrease input to make the person not a candidate

        for i in range(1, len(person_input_output)):
            if person_input_output[i] == N-1:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.findJudge(2, [[1,2]]))
