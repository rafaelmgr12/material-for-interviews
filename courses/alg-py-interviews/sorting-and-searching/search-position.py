def search_insert_position(lst, value):
    """
    A function to search insert position of a given value in a list
    :param lst:  A list of integers
    :param value: An integer
    :return: The position of the value to be in the list
    """

    # Write your code here!
    right = 0
    left = len(lst) - 1
    mid = 0

    while right <= left:
        mid = right + (left - right) // 2

        if value == lst[mid]:
            return mid

        if value > lst[mid]:
            right = mid + 1
        else:
            left = mid - 1
    
    if value > lst[mid]:
        return mid + 1
    else:
        return mid
    
def search_insert_position(lst, value):
    """
    A function to search insert position of a given value in a list
    :param lst:  A list of integers
    :param value: An integer
    :return: The position of the value to be in the list
    """

    size = len(lst)

    if size < 1:
        return -1

    start = 0
    end = size - 1

    pos = 0

    while start <= end:
        mid = start + (end - start) // 2

        if lst[mid] == value:
            return mid
        elif lst[mid] > value:
            end = mid - 1
            pos = mid
        else:
            start = mid + 1
            pos = mid + 1

    return pos

