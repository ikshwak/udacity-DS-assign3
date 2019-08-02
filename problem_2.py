def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == None or number == None:
        return -1
    return rotated_array_search_helper(input_list,0,len(input_list)-1,number)


def rotated_array_search_helper(input_list,l,h,number):
    if l > h:
        print("rotated search: " + str(number) +" not in the list")
        return -1

    mid = (l+h)//2
    if input_list[mid] == number:
        return mid

    if input_list[l] <= input_list[mid]:
        if number >= input_list[l] and number <= input_list[mid]:
            return rotated_array_search_helper(input_list,l,mid-1,number)
        return rotated_array_search_helper(input_list,mid+1,h,number)

    if number >= input_list[mid] and number <= input_list[h]:
        return rotated_array_search_helper(input_list,mid+1,h,number)
    return rotated_array_search_helper(input_list,l,mid-1,number)
    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    print("Linear search: " + str(number) +" not in the list")
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    linearIdx = linear_search(input_list, number)
    print("Linear search index " + str(linearIdx))
    rotatedIdx = rotated_array_search(input_list, number)
    print("Rotated search index " + str(rotatedIdx))


"""
TEST CASE 1
"""
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
"""
Result:
Linear search index 0
Roated search index 0
"""

"""
TEST CASE 2
"""
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
"""
Result:
Linear search index 5
Roated search index 5
"""

"""
TEST CASE 3
"""
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
"""
Result:
Linear search index 2
Roated search index 2
"""

"""
TEST CASE 4
"""
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
"""
Result:
Linear search index 3
Roated search index 3
"""

"""
TEST CASE 5
"""
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
"""
Result:
Linear search: 10 not in the list
Linear search index -1
rotated search: 10 not in the list
Roated search index -1
"""

"""
TEST CASE 6
"""
test_function([[], -1])
"""
Result:
Linear search: -1 not in the list
Linear search index -1
rotated search: -1 not in the list
Roated search index -1
"""

"""
TEST CASE 7
"""
test_function([[6, 7, 8, 1, 2, 3, 4], -1])
"""
Result:
Linear search: -1 not in the list
Linear search index -1
rotated search: -1 not in the list
Roated search index -1
"""

"""
TEST CASE 8
"""
test_function([[6, 7, 8, 1, 2, 3, 4], None])
"""
Result:
Linear search: None not in the list
Linear search index -1
Roated search index -1
"""
