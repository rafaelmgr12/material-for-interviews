## Bubble Sort

def sort_binary_list_bubble(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """
    size = len(lst) # Store the size of the list

    for i in range(size): # Iterate through the list
        for j in range(0, size-i-1): # Iterate through the list

            #traverse of the list from 0 to size-i-1
            # Swap if the element is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j] # Swap the elements
        return lst
    

## Swapping 1s

def sort_binary_list_swap(lst):
    j = 0

    for i in range(len(lst)):
        if lst[i] < 1: # Swapping with jth element if the number is less than 1
            lst[i], lst[j] = lst[j], lst[i] # Swapping
            j += 1 # Incrementing j

    return lst