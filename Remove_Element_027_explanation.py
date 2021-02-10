# Confused why the returned value is an integer but your answer is an array?
# why list.remove() work ?

# Note that the input array is passed in by reference,
# which means modification to the input array will be known to the caller as well.
a = b = [1, 1, 2, 4]
b.remove(1)
print('a', a)
print('b', b)
