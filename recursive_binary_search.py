def recursive_binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == mid:
            return True
        elif target < data[mid]:
            return recursive_binary_search(data, target, low, mid - 1)
        else:
            return recursive_binary_search(data, target, mid + 1, high)

a = [1, 2, 3, 4, 5]
print(recursive_binary_search(a, 4, 0, 4))
print(recursive_binary_search(a, -1, 0, 4))

