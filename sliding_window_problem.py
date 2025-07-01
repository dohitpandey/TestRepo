def sliding_window_median(arr, k):
    result = []
    for i in range(len(arr)):
        if i + k > len(arr):
            break
        window = arr[i:i + k]
        window.sort()
        result.append(window[int(k / 2)]) if k % 2 != 0 else result.append(
            (window[int(k / 2)] + window[int(k / 2) - 1]) / 2)
    print(result)
    return result


if __name__ == '__main__':
    print(sliding_window_median([1, 3, -1, -3, 5, 3, 6, 7], 3))
    sliding_window_median([1, 2], 1)
    sliding_window_median([1, 2, 3, 4], 2)
