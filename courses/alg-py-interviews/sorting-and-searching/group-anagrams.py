def anagrams(lst):
    """
    Function to find anagram pairs
    :param lst: A lst of strings
    :return: Group of anagrams
    """
    
    # Empty dictionary which holds subsets of all anagrams together
    dictionary = {}

    # traversing all the lst strings
    for string in lst:

        # sorting the lst string and storing it in a key
        key = ''.join(sorted(string))

        # if the key is already in the dictionary then appending the original lst(Anagram).
        if key in dictionary.keys():
            dictionary[key].append(string)
            
        else:  # If there is no key in the dictionary
            dictionary[key] = []
            dictionary[key].append(string)

    # traversing the whole dictionary and concatenating values and keys
    result = []
    for key, value in dictionary.items():
        if len(value) >= 2:
            result.append(value)

    result = sorted(result) # sort the list

    return result


# Driver to test above code
if __name__ == '__main__':

    lst = ['tom marvolo riddle ', 'abc', 'def', 'cab', 'fed', 'clint eastwood ', 'i am lord voldemort', 'elvis', 'old west action', 'lives']
    print (anagrams(lst))
    