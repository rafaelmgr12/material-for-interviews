## Brute Force Solution

def find_sum_brute_force(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == n and i != j:
                return [lst[i], lst[j]]

## Sorting Solution
def find_sum_sortings(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    # Write your code here!
    order_lst = sorted(lst)
    left = 0
    right = len(order_lst) - 1
    while left < right:
        if order_lst[left] + order_lst[right] == n:
            return [order_lst[left], order_lst[right]]
        elif order_lst[left] + order_lst[right] < n:
            left += 1
        else:
            right -= 1
    return None

# Using a Dictionary
def find_sum_dict(lst,n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    found_values = {}

    for ele in lst:
        try:
            found_values[n - ele]
            return [n - ele, ele]
        except:
            found_values[ele] = 0

    return 

# Using the python set()
def find_sum_ele(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    found_values = set()

    for ele in lst:
        if n - ele in found_values:
            return [n - ele, ele]
        found_values.add(ele)

    return False