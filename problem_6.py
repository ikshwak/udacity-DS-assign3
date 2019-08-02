class minmax:
    def __init__(self,val1='',val2=''):
        self.max = val1
        self.min = val2


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None or len(ints) == 0:
       return None

    if len(ints) == 1:
        return tuple((ints[0], ints[0]))

    mmVal = minmax()
    if ints[0] >= ints[1]:
        mmVal.max = ints[0]
        mmVal.min = ints[1]
    else:
        mmVal.min = ints[0]
        mmVal.max = ints[1]

    index = 2
    while index < len(ints):
        if ints[index] <= mmVal.min:
            mmVal.min = ints[index]
        if ints[index] >= mmVal.max:
            mmVal.max = ints[index]
        index += 1

    return tuple((mmVal.min,mmVal.max))

## Example Test Case of Ten Integers
import random
"""
TEST CASE 1
"""
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
"""
Result:
Pass
"""

"""
TEST CASE 2
"""
l = [i for i in range(10, 10000)]  # a list containing 10 - 9999
random.shuffle(l)
print ("Pass" if ((10, 9999) == get_min_max(l)) else "Fail")
"""
Result:
Pass
"""

"""
TEST CASE 3
"""
l = [i for i in range(-10, 10000)]  # a list containing -10 - 9999
random.shuffle(l)
print ("Pass" if ((-10, 9999) == get_min_max(l)) else "Fail")
"""
Result:
Pass
"""

"""
TEST CASE 4
"""
l = [1,1,1,1,1,1,1,1,1,1,1,1]  # a list containing 1 - 1
print ("Pass" if ((1,1) == get_min_max(l)) else "Fail")
"""
Result:
Pass
"""

"""
TEST CASE 5
"""
l = []  # a list containing None
print ("Pass" if (None == get_min_max(l)) else "Fail")
"""
Result:
Pass
"""
