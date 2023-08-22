def merge_sort(list_data):
    if len(list_data) <= 1:
        return list_data

    mid = len(list_data) // 2
    left_half = list_data[:mid]
    right_half = list_data[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    result.extend(left)
    result.extend(right)

    return result


unsorted_list = [3, 4, 5, 22, 2, 78, 4, 3]

print(merge_sort(unsorted_list))
