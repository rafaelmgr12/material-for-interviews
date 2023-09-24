def dutch_national_flag(lst):
    """
    A function to solve Dutch National Flag Problem
    :param lst: A list of integers
    :return: A list of solved Dutch National Flag Problem
    """

    # Write your code here!
    return quick_sort(lst)

def quick_sort(lst):
    """
    A function to sort a list using quicksort algorithm
    :param lst: A list of integers
    :return: A sorted list
    """
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = []
        right = []
        for i in range(1, len(lst)):
            if lst[i] < pivot:
                left.append(lst[i])
            else:
                right.append(lst[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
    
# Three-way partitioning
def dutch_national_flag(lst):
    """
    A function to solve Dutch National Flag Problem
    :param lst: A list of integers
    :return: A list of solved Dutch National Flag Problem
    """

    size = len(lst)
    i = 0
    mid = 0
    j = size - 1

    while mid <= j:
        if lst[mid] == 0:
            lst[i], lst[mid] = lst[mid], lst[i]
            i += 1
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[j] = lst[j], lst[mid]
            j -= 1
        elif lst[mid] == 1:
            mid += 1

    return lst
