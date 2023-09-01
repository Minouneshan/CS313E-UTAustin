#  File: DNA.py

#  Description: 
#      DNA has played an important role in research in computer science.
#  For example research in string searching algorithms has been motivated by finding sequences in DNAs.
#  For the present project, we are interested in finding the longest common base sequence in two DNA strands.
#  Each strand is represented by the sequence of letters A, T, C, and G.
#  For the two strands ACTG and TGCA the longest common sequence is TG.
#  It is quite possible for two strands not to have any common sequence (a sequence of 1 base does not count).
#  Also there could be two or more common sequences that have the same longest length.
#    Input: The first line of data is an integer number n that gives the number of pairs of DNA to follow.
# We will read one pair of DNA strings at a time.
# The maximum length of each string is 80 characters.
# We Assume that each string consists only of characters 'A', 'T', 'C' and 'G'.
#    Output: Print out the longest common sequence(s) for the two strings.
# If there is more than one longest common sequence then it prints each of those sequences on separate lines in alphabetical order.

#  Student Name: Mohamad Minoneshan

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 8/28/2022

#  Date Last Modified: 8/29/2022

import sys

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

def longest_subsequence (s1, s2):
    # defining variables for: the list,
    # the subsequence, longest and shortest subsequences from the pairs
    long_sub = []
    sub = ''
    long_s  = max(s1,s2)
    short_s = min(s1,s2)

    # 
    for i in range(len(short_s)):
        for j in range(len(long_s)):
            w = i; u = j
            while long_s[u] == short_s[w]:
                sub += short_s[w]
                u += 1 ; w += 1

                if (u == len(long_s)) or (w == len(short_s)):
                    break

            if sub != '':
                    if len(long_sub) == 0:
                         long_sub.append(sub)
                         sub = ''
                    elif len(long_sub[0]) > len(sub):
                         sub = ''
                    elif len(long_sub[0]) == len(sub):
                         long_sub.append(sub)
                         sub = ''
                    else:
                         long_sub = []
                         long_sub.append(sub)
                         sub = ''
    # using built-in sort function for the list
    long_sub = sorted(long_sub)
    return long_sub

def main():
  # read the number of pairs
    num_pairs = sys.stdin.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int (num_pairs)

  # for each pair call the longest_subsequence
    for i in range (num_pairs):
        st1 = sys.stdin.readline()
        st2 = sys.stdin.readline()

        st1 = st1.strip()
        st2 = st2.strip()

        st1 = st1.upper()
        st2 = st2.upper()

    # get the longest subsequences
        long_sub = longest_subsequence (st1, st2)

    # print the result
        print('Longest matching subsequence for the Pairs:',st1,st2,'\n')    
        if len(long_sub) != 0:
            for i in long_sub:
                print(i)
            else:
                print('No Common Sequence Found')

        # insert blank line
        print('\n')

if __name__ == "__main__":
  main()
