#  File: Cipher.py

#  Description:Cryptography is an ancient study of secret writing.
#  There is a wealth of literature in this field.
#  An extremely readable book on this subject is The Code Book by Simon Singh.
#  This is a field of study that is of particular relevance in Computer Science.
#  Given the widespread use of computers,
#  one of the things people are interested in is making transactions over the internet more secure.
#  Here is a simple and clever way to encrypt plain text.
#  We Assume that the message contains only upper case letters,
#  lower case letters and digits. Let L be the length of the original message,
#  And M the smallest square number greater than or equal to L.
#  We add (M-L) asterisks to the message, giving a padded message with length M.
#  Then we use the padded message to fill a table of size K x K, where K2 = M.
#  We fill the table in row-major order (left to right in each column, top to bottom for each row).
#  Now to encrypt, rotate the table 90° clockwise.
#  The encrypted message comes from reading the message in row-major order from the rotated table,
#  omitting any asterisks and maintaining the case of each character from the original message.

#  Student Name: Mohamad Minoneshan

#  Partner Name: paulina Brown

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/11/2022

#  Date Last Modified: 9/12/2022

import sys
import math


def string_to_list2d(strng):
    y = int(math.sqrt(len(strng)))
    if (len(strng) - y*y):
        y += 1
    z = y*y - len(strng)
    while z > 0:
        strng += '*'
        z -= 1
    li = [i for j, i in enumerate(strng)]
    li_2d = []
    for i in range(y):
        li_2d.append(li[i*y:(i+1)*y])
    return li_2d


def list2d_to_string(list2d):
    strng = ''
    for row in list2d:
        for i in row:
            strng += i
    strng = strng.replace('*', "")

    return strng

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string


def encrypt(strng):
    li_2d = string_to_list2d(strng)
    rotated = [list(reversed(col)) for col in zip(*li_2d)]
    strng_out = list2d_to_string(rotated)
    return strng_out

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string


def decrypt(strng):
    li_2d = string_to_list2d(strng)
    c_rotated = [[li_2d[j][i] for j in range(
        len(li_2d))] for i in range(len(li_2d[0])-1, -1, -1)]
    strng_out = list2d_to_string(c_rotated)

    return strng_out


def main():
  # read the two strings P and Q from standard imput
    P = sys.stdin.readline()
    P = P.strip()
    Q = sys.stdin.readline()
    Q = Q.strip()
  # encrypt the string P
    enc_P = encrypt(P)
  # decrypt the string Q
    dec_Q = decrypt(Q)
  # print the encrypted string of P and the
  # decrypted string of Q to standard out

    sys.stdout.write(enc_P+'\n'+dec_Q+'\n')


if __name__ == "__main__":
    main()
