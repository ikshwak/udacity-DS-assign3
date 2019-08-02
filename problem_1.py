def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print("Not a positive integer")
        return None

    if number == 0 or number ==1:
        return number

    start = 1
    end = number
    sqrt = 0
    while start <= end:
        mid = (start+end)//2
        if mid*mid == number:
            sqrt = mid
            return sqrt
        elif mid*mid < number:
            start = mid + 1
            sqrt = mid
        else:
            end = mid - 1
    return sqrt


"""
TEST CASE 1
"""
print("TEST CASE 1")
print(sqrt(9))
"""
Result:
TEST CASE 1
3
"""

"""
TEST CASE 2
"""
print("TEST CASE 2")
print (sqrt(0))
"""
Result:
TEST CASE 2
0
"""

"""
TEST CASE 3
"""
print("TEST CASE 3")
print (sqrt(-1))
"""
Result:
TEST CASE 3
Not a positive integer
None
"""

"""
TEST CASE 4
"""
print("TEST CASE 4")
print (sqrt(1))
"""
Result:
TEST CASE 4
1
"""

"""
TEST CASE 5
"""
print("TEST CASE 5")
print (sqrt(27))
"""
Result:
TEST CASE 5
5 --> Value floored to the nearest positive integer
"""
