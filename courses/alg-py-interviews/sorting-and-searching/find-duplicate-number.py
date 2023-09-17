
# Brute Force Approach
def find_duplicates(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """

    result = []  # A list to store duplicates

    # Write your code here!
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in result:
                result.append(lst[i])
    return result


 # if already counted and dictionary in action
def find_duplicates_dict(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """

    result = []  # A list to store duplicates

    seen = {} # A dictionary to store already observed elements

    for x in lst:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                result.append(x)
            seen[x] += 1
    return result