
#  File: Boxes.py

#  Description: Given a set of boxes, this program determines how many of the boxes
#               can be nested inside one another. It returns the number of boxes that
#               can be nested as well as how many combinations of different
#               boxes are able to achieve it.

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/16/2022

#  Date Last Modified: 10/18/2022

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):

  # insert the [0, 0, 0] box into the box list so that it may match
  # the indices of the memo
  box_list.insert(0, [0 ,0, 0])

  # create a memo with default values, including the [0, 0, 0] box
  # n is the maximum number of boxes that fit in box i
  # max_now is the current maximum number of nested boxes
  # r is the index of the largest box that has max_now
  # num_ways is the number of ways that n can be achieved
  memo = []
  n = 0; max_now = 0; r = 0; num_ways = 1
  memo.append([n, max_now, r, num_ways])
  for x in range(len(box_list) - 1):
    memo.append([0, 0, 0, 0])

  # create a double loop, the outer loop moves down the list of boxes
  for i in range(1, len(memo)):

    # initialize n, the start of the search and the end of the search
    n = memo[i][0]
    start_check = i - 1
    end_check = -1

    # the inner loop checks if any of the previous boxes can be nested
    for j in range(start_check, end_check, -1):

      if does_fit(box_list[j], box_list[i]):

        # if box[j] fits inside box[i] and the new value of n is greater than the previous
        # value of n, update the value of n and store the number of ways n can be achieved
        if (memo[j][0] + 1 > n):
          n = memo[j][0] + 1
          memo[i][3] = memo[j][3]

        # else if the new value of n is equal to the previous value of n, add to the number
        # of ways that n can be achieved
        elif (memo[j][0] + 1 == n):
          memo[i][3] += memo[j][3]

    # update the memo with the final value of n
    memo[i][0] = n

    # if the value of n is above the global max, update the global max and the index where
    # it is found or keep the current global max and global max index
    if memo[i][0] >= max_now:
      max_now = memo[i][0]
      memo[i][1] = max_now
      r = i
      memo[i][2] = r
    else:
      memo[i][1] = max_now
      memo[i][2] = r

  # the last list in the memo will always contain the global max
  max_boxes = memo[-1][1]

  # if n is equal to the global max, add the number of ways to
  # achieve n to the total number of maximizing combinations
  count = 0
  for i in range(len(memo)):
    if memo[i][0] == max_boxes:
      count = count + memo[i][3]

  return max_boxes, count


# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  #print (box_list)
  #print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  #print (box_list)
  #print()

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (box_list)

  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print (num_sets)

if __name__ == "__main__":
  main()

