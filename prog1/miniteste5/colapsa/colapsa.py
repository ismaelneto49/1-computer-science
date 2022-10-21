def colapsa_n_menores(N, nums):
    sum = 0
    for a in range(N):
        smallest = nums[0]
        index = 0
        for i in range(len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
                index = i
        nums.pop(index)
        sum += smallest
    nums.append(sum)
