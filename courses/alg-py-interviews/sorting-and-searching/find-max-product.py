# Decimal library to assign infinite numbers
from decimal import Decimal

# Personal Solution
def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    # Write your code here!
    sorted_lst = sorted(lst)
    if sorted_lst[0] < 0 and sorted_lst[1] < 0:
        return sorted_lst[0], sorted_lst[1]
    else:
        return sorted_lst[-1], sorted_lst[-2]
    

# Brute Force Approach  
# Decimal library to assign infinite numbers

def find_max_prod_brute(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    max_product = Decimal('-Infinity')
    max_i = -1
    max_j = -1

    for i in lst:
        for j in lst:
            if max_product < i * j and i is not j:
                max_product = i * j
                max_i = i
                max_j = j

    return max_i, max_j

# traversing the list once
def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    max1 = lst[0]
    max2 = Decimal('-Infinity')

    min1 = lst[0]
    min2 = Decimal('Infinity')

    for number in lst:

        if number > max1:
            max2 = max1  # Second highest
            max1 = number  # First highest
        elif number > max2:
            max2 = number

        if number < min1:
            min2 = min1  # Second lowest
            min1 = number  # First lowest
        elif number < min2:
            min2 = number

    # Checking which pair has the highest product
    if max1 * max2 > min1 * min2:
        return max2, max1
    else:
        return min2, min1
