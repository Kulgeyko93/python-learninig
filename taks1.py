init_array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def get_numbers_more_than_five(array):
    result = []
    for item in array:
        value = item
        if item > 5:
            result.append(item)
    return result


print(get_numbers_more_than_five(init_array))
