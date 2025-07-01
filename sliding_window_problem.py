def sliding_window_median(arr, k):
    result = []
    for i in range(len(arr)):
        if i+k>len(arr):
            break
        window = arr[i:i+k]
        window.sort()
        result.append(window[1])
    # print(result)
    return result


if __name__ == '__main__':
    print(sliding_window_median([1,3,-1,-3,5,3,6,7],3))
