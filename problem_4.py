def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list == None:
        return []

    start = 0
    end = len(input_list)-1
    mid = 0

    while mid <= end:
        if input_list[mid] == 0:
            input_list[start],input_list[mid] = input_list[mid],input_list[start]
            start += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        elif input_list[mid] == 2:
            input_list[end],input_list[mid] = input_list[mid],input_list[end]
            end -= 1
        else:
            print("invalid 012 list")
            return []

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print("Solution: " + str(sorted_array))
    print("Library sort: " + str(sorted(test_case)))


"""
TEST CASE 1
"""
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
"""
Result:
Solution: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
Library sort: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
"""

"""
TEST CASE 2
"""
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
"""
Result:
Solution: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Library sort: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
"""

"""
TEST CASE 3
"""
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
"""
Result:
Solution: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
Library sort: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
"""

"""
TEST CASE 4
"""
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 3])
"""
Result:
invalid 012 list
Solution: []
Library sort: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4]
"""

"""
TEST CASE 5
"""
test_function([])
"""
Result:
Solution: []
Library sort: []
"""
