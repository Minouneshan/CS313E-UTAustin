#  File: Tower.py

#  Description: 

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/13/2022

#  Date Last Modified: 10/14/2022

import sys
import math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
    x = 2
    while math.comb(x,2) <= n:
        x += 1
    k = n - math.comb(x-1,2)
    return ((2**(x-2)) * (k + x - 3)) + 1

def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()

