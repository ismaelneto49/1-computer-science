def move(index, count, element, array):
    for j in range(index, len(array)- 1):
        array[j] = array[j+1]
    array[-1] = element


def aparta(nums, k):
    count = 0
    for n in nums:
        if n % k == 0:
            count += 1

    if count == len(nums) or count == 0: return nums

    for i in range(len(nums)-count+1, -1, -1):
        if nums[i] % k == 0:
            move(i, count, nums[i], nums)
            
    for r in range(count):
        for t in range(len(nums)-1, count+r, -1):
            temp = nums[t]
            nums[t] = nums[t-1]
            nums[t-1] = temp
    

    return count

a = [1,2,3,4,5,6]
print(a)
print(aparta(a,2))
print(a)

v = [8, 10, 11, 7, 21, 2, 17, 6, 28, 24]
print(v)
print(aparta(v,3))
print(v)
