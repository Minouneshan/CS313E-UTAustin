#  File: Spiral.py

#  Description: Consider the natural numbers laid out in a square spiral,
#  with 1 occupying the center of the spiral. This spiral has several interesting features. 
#  The southeast diagonal has several prime numbers (3, 13, 31, 57, and 91) along it.
#  The southwest diagonal has a weaker concentration of prime numbers (5, 17, 37) along it.
#  To construct the spiral we start with 1 at the center, with 2 to the right, and 3 below it,
#  4 to the left, and so on. 
#  We will read your input data from a file called spiral.in. The first line will be the dimension of the spiral.
#  It will always be odd and greater than 1 and less than 100. 
#  This will be followed by an arbitrary number of lines. There will be a single number on each line.
#  And for Output, For each of the numbers inside the spiral,
#  your output will be the sum of all the numbers adjacent to this number, but not including this number.

#  Student Name: Mohamad Minoneshan

#  Partner Name: paulina Brown

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 8/30/2022

#  Date Last Modified: 9/2/2022

import sys


# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral ( n ):
    # if n in even then add one to n
    if n >0  and n % 2 == 0:
        n += 1
    # if n is less than or equal to hundred then run the code
    if 0 < n and n <= 100:
        spiral = []
        # create the point number '1' and append its location to spiral 
        x = n//2 + 1
        y = n//2 + 1
        spiral.append([x,y])
        step = 1
        # At each loop, we go all way horizontal and one way vertical. 
        # the number of steps increase by increasing in the loop. 
        for i in range(1,n):
            for j in range(i):
                x += step
                spiral.append([x,y])
            for j in range(i):
                y -= step
                spiral.append([x,y])   
            # multiplying step by -1 to change the direction
            step *= -1
        # Lastly, the top row is remaind which we add another loop to cover that    
        for i in range(1,n):
            x += step
            spiral.append([x,y])       
    return spiral

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
    step = 1
    lst = []
    for i in range(1,len(spiral)+1):
        lst.append(i)
    x,y = spiral[lst.index(n)][0], spiral[lst.index(n)][1]
    sum = 0
    # the same algorithm from the spiral function, just a spiral with dimension of 3*3
    for i in range(1,3):
        for j in range(i):
            x += step
            try:
                sum += lst[spiral.index([x, y])]
            except ValueError:
                pass
        for j in range(i):
            y -= step
            try:
                sum += lst[spiral.index([x, y])]  
            except ValueError:
                pass
        step *= -1
    
    step = 1
    for j in range(1,3):
        x += step
        try:
            sum += lst[spiral.index([x, y])] 
        except ValueError:
            pass  

    return sum

def main():
    # read the input file
    dim = sys.stdin.readline()
    dim = dim.strip()
    dim = int (dim)
    # create the spiral

    spiral = create_spiral(dim)

    # add the adjacent numbers
    adjacent = sys.stdin.readline()
    adjacent = adjacent.strip()
    # read new line as long it is not empty
    while adjacent != '':
      adjacent = int (adjacent)
      # if adjacent was out of the range, it will return zero
      if adjacent < dim*dim and adjacent > 0:
        sum = sum_adjacent_numbers(spiral, adjacent)
      else:
        sum = 0
      # print the result
      print(sum)
      adjacent = sys.stdin.readline()
      adjacent = adjacent.strip()

if __name__ == "__main__":
  main()





