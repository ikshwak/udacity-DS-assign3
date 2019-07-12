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
       return tuple(None,None)

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

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
