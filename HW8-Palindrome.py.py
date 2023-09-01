#  File: Palindrome.py

#  Description:

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/29/2022

#  Date Last Modified: 10/03/2022
import sys

def isPalindrome(s, i):
    if(i > len(s)/2):
        return True
    ans = False
    if((s[i] is s[len(s) - i - 1]) and isPalindrome(s, i + 1)):
        ans = True
    return ans


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    palindromes = []
    for i in range(len(str),-1,-1):
        x = str[len(str)-1:i:-1] + str
        if isPalindrome(x,0):
            palindromes.append(x)
    shortest_string = min(palindromes, key = len)

    return shortest_string  
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  
  assert smallest_palindrome('cbabcde') == 'edcbabcde'

  assert smallest_palindrome('a') == 'a'

  return "all test cases passed"

def main():
    # run your test cases
    
    #print (test_cases())
    

    # read the data
    palindromic_string  = sys.stdin.readline().strip()
    # print the smallest palindromic string that can be made for each input
    while palindromic_string != '':
      print(smallest_palindrome(palindromic_string))
      palindromic_string  = sys.stdin.readline().strip()
if __name__ == "__main__":
  main()