# This method of use is not very good

nums = [1, 2, 3, 4]

for i in range(len(nums) - 1, 0, -1):
    print('i', i)
    del nums[i]
    print('nums', nums)
