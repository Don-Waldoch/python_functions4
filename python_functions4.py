# Write a Python function called max_num()to find the maximum of three numbers.
# Write a Python function called mult_list() to multiply all the numbers in a list.
# Write a Python function called rev_string() to reverse a string.

# Write a Python function called num_within() to check whether a number falls in
# a given range. The function accepts the number, beginning of range, and end of
# range (inclusive) as arguments.
#   Examples: num_within( 3,2,4) returns True,
#             num_within( 3,1,3) returns True,
#             num_within(10,2,5) returns False.

def max_num(i, j, k):
    return max(i, j, k)


def mult_list(nums):
    product = 1
    for i in nums:
        product *= i
    return product


def rev_string(text):
    return text[::-1]


def num_within(i, j, k):
    return (j <= i and i <= k)

# Call each function


print(max_num(5, 3, 12))
print(mult_list([1, 4, 7, 2]))
print(rev_string("Hello World!"))
print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))
