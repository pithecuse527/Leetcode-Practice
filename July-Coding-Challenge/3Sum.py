def threeSum(self, nums):
    dict_of_nums = {num : nums.count(num) for num in nums}      # create hash map first
    to_return = []

    # for x in dict_of_nums:
    #     if dict_of_nums[x]:
    #         dict_of_nums[x] -= 1
    #         for y in dict_of_nums:
    #             if dict_of_nums[y]:
    #                 dict_of_nums[y] -= 1
    #                 if -(x+y) in dict_of_nums: to_return.append()
    #
    #             dict_of_nums[y] += 1
    #         dict_of_nums[key] += 1

    # todo1: only look forward (lst and dict)
    for i in range(len(nums) - 1):
        x = nums[i]
        if dict_of_nums[x]:
            dict_of_nums[x] -= 1
            tmp_nums = [i + 1:]
            for j in tmp_nums:
