def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list == None:
        return [0,0]
    input_list = mergesort(input_list)
    print(input_list)

    if len(input_list)%2 == 0:
        return rearrange_digits_even(input_list)

    else:
        return rearrange_digits_odd(input_list)

def rearrange_digits_even(input_list):
    firstNum = 0
    secondNum = 0
    print("rearrange_digits_even")
    index = 0

    while index < len(input_list)-1:
        firstNum = 10*firstNum + input_list[index]
        secondNum = 10*secondNum + input_list[index+1]
        index += 2

    firstNum = reverseInteger(firstNum)
    secondNum = reverseInteger(secondNum)
    return [firstNum,secondNum]
    

def rearrange_digits_odd(input_list):
    firstNum = 0
    secondNum = 0
    print("rearrange_digits_odd")
    
    index = 0

    while index < len(input_list)-2:
        firstNum = 10*firstNum + input_list[index]
        secondNum = 10*secondNum + input_list[index+1]
        index += 2

    secondNum = 10*secondNum + input_list[index]

    firstNum = reverseInteger(firstNum)
    secondNum = reverseInteger(secondNum)
    return [firstNum,secondNum]

def reverseInteger(intVal):
    if intVal == None:
        print("not a valid int value")
        return None

    if type(intVal) != int:
        print("not a valid int")
        return None

    reverse = 0
    while intVal:
        digit = intVal % 10
        reverse = reverse*10 + digit
        intVal //=10

    return reverse
    

def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

"""
2,4,5,6,8,9

1,2,3,4,5,6,7,8,9

98642 + 7531

Logic:

    1. sort the array in O(nlogn) time in descending order
    2. if the array has odd number of element add index 0,1 elements to a list
    3. followed by alternate elements from index 3 to another list
    3.5 create a number from the list and reverse it or create a number from the rear end of the list
    4. if array has even number of elements add even indexed elements to a list
    5. followed by odd indexed elements to another list
    5.5 create a number from the list and reverse it or create a number from the rear end of the list
"""
