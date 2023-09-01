#  File: Reducible.py

#  Description: This file finds the longest English words that remain
#               Valid English words as we remove one letter at a time from those words.
#               Input is a given file which connatains all the words we use as reference.

#  Student Name: Mohamad Minoneshan

#  Student UT EID: SM75774

#  Partner Name: Mercedes Milke

#  Partner UT EID: MM96327

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/20/2022

#  Date Last Modified: 10/21/2022


import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):

  hash_value = 0
  power26 = 1

  # computes the hash value for the string using powers of 26
  # converts each character into a number, multiplies it by
  # its respective power of 26 and adds it to the hash value
  for i in range(len(s) - 1, -1, -1):
    letter = ord(s[i]) - 96
    hash_value += power26 * letter
    power26 *= 26

  return const - (hash_value % const)

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  # determines the initial hash index
  size = len(hash_table)
  hash_index = hash_word(s, size)

  # determines the step size
  constant = 7
  step = step_size(s, constant)

  # if the hash table already has a string at the hash index,
  # adjusts the hash index using double hashing
  while (hash_table[hash_index] != ''):
    hash_index = hash_index + step
    hash_index = hash_index % size

  # inserts the string into the hash table
  hash_table[hash_index] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  # determines the hash index that the word should be at
  size = len(hash_table)
  hash_index = hash_word(s, size)

  # determines the step size for the string
  constant = 7
  step = step_size(s, constant)

  # the string has been found at its initially assigned hash index
  if hash_table[hash_index] == s:
    return True

  # if the hash table is not empty at the initial hash index, check
  # all other hash indices where the string could be found
  elif hash_table[hash_index] != '':
    while (hash_table[hash_index] != ''):
      hash_index = hash_index + step
      hash_index = hash_index % size
      if hash_table[hash_index] == s:
        return True

  # if the hash table at the initially assigned hash index is empty,
  # it means that the string is not in the hash table
  else:
    return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  # if the word can be reduced to 'a', 'i' or 'o',
  # it is a reducible word
  if (s == 'a' or s == 'i' or s == 'o'):
    return True

  # if the reduced word is in the hash memo,
  # no need to check any further
  elif (find_word(s, hash_memo)):
    return True

  # if the reduced word is not in the dictionary of
  # words, it is not reducible
  elif not find_word(s, hash_table):
    return False

  else:

    # iterate through the word, removing one letter at a time
    for i in range(len(s)):
      modified_str = s[:i] + s[i + 1:]

      # if the word is reducible, add it to the hash memo
      if is_reducible(modified_str, hash_table, hash_memo):
        insert_word(s, hash_memo)
        return True

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  max_length = 0
  longest_words = []

  # find the length of the longest word
  for word in string_list:
    if len(word) > max_length:
      max_length = len(word)

  # add each word that is the same length as the longest word
  # to the list of longest words
  for word in string_list:
    if len(word) == max_length:
      longest_words.append(word)

  return longest_words

def main():
  # create an empty word_list
  word_list = []
  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list
  list_len = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  n_prime = 2 * list_len
  while is_prime(n_prime) == False:
    n_prime += 1

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for i in range(0, n_prime):
    blank_string = ''
    hash_list.append(blank_string)

  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for word in word_list:
    insert_word(word, hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than
  # 0.2 * size of word_list
  m_prime = round(0.2 * list_len)
  while is_prime(m_prime) == False:
    m_prime += 1

  # populate the hash_memo with M blank strings
  hash_memo = []
  for i in range(0, m_prime):
    blank_string = ''
    hash_memo.append(blank_string)

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for word in word_list:
    if is_reducible (word, hash_list, hash_memo):
      reducible_words.append(word)

  # find the largest reducible words in reducible_words
  largest_words = get_longest_words(reducible_words)

  # print the reducible words in alphabetical order
  # one word per line
  largest_words.sort()
  for word in largest_words:
    print(word)

if __name__ == "__main__":
  main()