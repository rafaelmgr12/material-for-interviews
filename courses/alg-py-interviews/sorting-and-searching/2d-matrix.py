
# Brute Force always works!
def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    # Write your code here!
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == number:
                return True
    return False


# Binary Search
def find_in_binary_search(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    # Write your code here!
    rows = len(lst)

    if lst is None or row == 0:
        return False
    
    cols = len(lst[0])

    if cols == 0:
        return False
    
    i = 0
    j = rows -1
    if rows > 1:
        while i <= j:
            mid = i + (j - i) // 2
            if number == lst[mid][cols - 1]:
                return True

            if number > lst[mid][cols - 1]:
                i = mid + 1
            else:
                j = mid - 1

        if number > lst[mid][cols - 1]:
            rows = mid + 1
        else:
            rows = mid
    else:
        rows = 0

    if rows >= len(lst):
        return False

    i = 0
    j = cols - 1

    while i <= j:
        mid = i + (j - i) // 2
        if number == lst[rows][mid]:
            return True

        if number > lst[rows][mid]:
            i = mid + 1
        else:
            j = mid - 1

    return False