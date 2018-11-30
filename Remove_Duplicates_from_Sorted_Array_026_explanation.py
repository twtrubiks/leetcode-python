# This method of use is not very good

nums = [1, 2, 3, 4]

for i in range(len(nums) - 1, 0, -1):
    print('i', i)
    del nums[i]
    print('nums', nums)

# Confused why the returned value is an integer but your answer is an array?
# nums=[1,1,2]  , return len(set(nums))  ,  output  [1,1] ?

# because will check nums too see if it's content is correct,
# but will check only the first n (the number that you returned) elements.

# Note that the input array is passed in by reference,
# which means modification to the input array will be known to the caller as well.

# why del work ?
a = b = [1, 1, 2, 4]
del b[2]
print('a', a)
print('b', b)

a1 = b1 = [1, 1, 2, 4]
print('a1', a1)
print('set(b1)', set(b1))
