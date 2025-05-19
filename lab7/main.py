def kadane(arr):
    curr_sum = 0
    max_sum = 0
    for item in arr:
        if curr_sum < item:
            curr_sum = 0
        curr_sum += item
        if max_sum < curr_sum:
            max_sum = curr_sum
    return max_sum
        


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    #print(kadane(arr))
    a = 15 ** 101
    b = 45 ** 3 * 8 ** 5 * 75
    print(b % 103)