#  File: Work.py 

#  Description: This File finds the minimum number which the sum of 
#  x // i**2 exceeds n. 

#  Student Name: Mohamad Minoneshan

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/27/2022

#  Date Last Modified: 9/27/2022

import sys, time

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  # use linear search here
    i = 0
    x = True
    while x:
        s = 0
        j = 0
        while i//k**j > 0 and s < n:
            s += i//k**j
            j += 1
        if s >= n:
            x = False
            return i 
        i += 1


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
    lo = 1
    hi = n
    li = []
    while (lo <= hi):
        mid = (lo + hi)//2
        s = 0
        j = 0
        while mid//k**j > 0:
            s += mid//k**j
            j += 1
        if (n > s):
            lo = mid + 1
        elif (n < s):
            hi = mid - 1
            li.append(mid)
        else:
            return mid
    return min(li)

# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
