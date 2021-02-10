
def trunk_1(arr_1, size_1):
    result_1 = []
    while arr:
        pop_data = [arr_1.pop(0) for _ in range(size_1)]
        result_1.append(pop_data)
    return result_1


def trunk_2(arr_2, size_2):
    arrs = []
    while len(arr_2) > size_2:
        pice = arr_2[:size_2]
        arrs.append(pice)
        arr_2 = arr_2[size:]
    arrs.append(arr_2)
    return arrs


def trunk_3(arr, size):
    result = []

    count = 0
    while count < len(arr):
        result.append(arr[count:count+size])
        count += size
    return result


if __name__ == "__main__":
    '''
    arr = [1, 2, 3, 4, 5, 6]
    size = 2
    result = [[1, 2], [3, 4], [5, 6]]
    '''
    arr = [1, 2, 3, 4, 5, 6]
    size = 2
    result = trunk_1(arr, size)
    print(result)
