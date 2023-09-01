
#  File: Radix.py

#  Description: This program sorts a list of strings containing both characters and numbers
#               using the Radix Sort algorithm.

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/23/2022

#  Date Last Modified: 10/24/2022

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a list of strings containing both lower case letters and digits
# Output: a list of strings of the same length as padding has been
#         added to the shorter strings
def pad_strings(eid_list):

    # find the length of the longest string
    longest_string = max(eid_list, key = len)
    longest_length = len(longest_string)

    # pad strings that are shorter than the longest string
    padded_strings = []
    for eid in eid_list:
        pad = len(longest_string) - len(eid)
        new_string = eid + '!' * pad
        padded_strings.append(new_string)

    # return the list of padded strings
    return padded_strings

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  # create the Queue objects
  queue_list = [Queue() for i in range (38)]

  # find the number of passes
  longest_string = max(a, key=len)
  num_passes = len(longest_string) - 1

  # create a dictionary which each character as a key
  # and its index as the value
  char_dict = {}

  # add the padding key
  char_dict.update({'!': 0})

  # add the number keys
  for i in range(10):
      char_dict[str(i)] = i

  # add the letter keys
  for i in range(26):
      char_dict.update({chr(i + 97): i + 10})

  # put all the eid strings into the last queue
  for eid in a:
      queue_list[-1].enqueue(eid)

  # do the passes, moving from the last index of
  # each string to the first
  for i in range(num_passes, -1, -1):

    # move the strings from the last queue to their
    # respective queues based on the character
    # at the string index
    while not queue_list[-1].is_empty():
      eid = queue_list[-1].dequeue()
      eid_index = eid[i]
      position = char_dict[eid_index]
      queue_list[position].enqueue(eid)

    # move the strings to the last queue by iterating
    # through each queue in order and adding its
    # strings to the last queue
    for j in range(len(queue_list) - 1):
      while not queue_list[j].is_empty():
          eid = queue_list[j].dequeue()
          queue_list[-1].enqueue(eid)

  # move the sorted strings from the last queue to a new list
  sorted_list = []
  while not queue_list[-1].is_empty():
      eid = queue_list[-1].dequeue()
      sorted_list.append(eid)

  # remove the padding character from the sorted strings
  clean_list = []
  for eid in sorted_list:
      final_eid = eid.translate({ord(c): None for c in '!'})
      clean_list.append(final_eid)

  # return the sorted list
  return clean_list

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  # pad the strings
  modified_list = pad_strings(word_list)

  # use radix sort to sort the word_list
  sorted_list = radix_sort (modified_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    
