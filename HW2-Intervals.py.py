#  File: Intervals.py

#  Description:

#  Student Name: Mohamad Minoneshan

#  Partner Name: paulina Brown

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/9/2022

#  Date Last Modified: 9/9/2022

import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval


def merge_tuples(tuples_list):

    # Input: tuples_list is a list of tuples denoting intervals
    # Output: a list of tuples sorted by ascending order of the size of
    #         the interval
    #         if two intervals have the size then it will sort by the
    #         lower number in the interval
    # Sort the array on the basis of start values of intervals.

    # Convert the tuple to list first
    C_list = []
    for i in tuples_list:
        C_list.append(list(i))
    C_list

    C_list.sort()
    stack = []
    # insert first interval into stack
    stack.append(C_list[0])
    for i in C_list[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][1]:
            stack[-1][1] = max(stack[-1][1], i[-1])
        else:
            stack.append(i)
    # Convert the list to tuple
    C_tuple = []
    for i in stack:
        C_tuple.append(tuple(i))

    return C_tuple

# sort the tuple interval based on the size of the interval


def sort_by_interval_size(tuples_list):
    tuples_list.sort(key=lambda l: abs(l[0] - l[1]))
    return tuples_list

# Input: no input
# Output: a string denoting all test cases have passed


def test_cases():
    assert merge_tuples([(1, 2)]) == [(1, 2)]
    # write your own test cases

    assert sort_by_interval_size([(1, 3), (4, 5)]) == [(4, 5), (1, 3)]
    # write your own test cases

    return "all test cases passed"


def main():
    # open file intervals.in and read the data and create a list of tuples
    size = sys.stdin.readline()
    size = size.strip()
    size = int(size)
    tuple_list = []
    for i in range(size):
        x, y = map(int, sys.stdin.readline().split())
        tuple_list.append((x, y))

# merge the list of tuples
    tuple_list = merge_tuples(tuple_list)
    print('{}'.format(tuple_list))
# sort the list of tuples according to the size of the interval
    tuple_list = sort_by_interval_size(tuple_list)

# run your test cases

   # print(test_cases())

# write the output list of tuples from the two functions
    print('{}'.format(tuple_list))


if __name__ == "__main__":
    main()
