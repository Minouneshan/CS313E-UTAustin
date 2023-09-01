#  File: BST_Cipher.py

#  Description: This program encrypts and decrypts strings using a binary search tree.

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/10/2022

#  Date Last Modified: 11/10/2022


import sys

class Node(object):
    def __init__(self, data = None, lchild = None, rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):

        # construct the root
        self.root = None

        # traverse through the string and add each character to the binary tree
        for ch in encrypt_str:
            ascii_val = ord(ch.lower())
            if ((ascii_val >= 97 and ascii_val <= 122)):
                self.insert(ch)
            elif (ascii_val == 32):
                self.insert(ch)
            else:
                continue

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):

        # create a new node
        new_node = Node(ch)

        # initialize the search
        current = self.root
        parent = self.root

        # if the tree is empty, make the new node the root
        if (self.root == None):
            self.root = new_node

        # traverse through the tree to reach its leaves with the
        # traversal direction being determined by the node value
        else:
            while (current != None):
                parent = current

                # if a node with the character is already in the tree,
                # no need to insert it again
                if (ch == current.data):
                    break

                # go left
                elif (ch < current.data):
                    current = current.lchild

                # go right
                elif (ch > current.data):
                    current = current.rchild

            # insert the new node as a left child of one of the leaves
            if (ch < parent.data):
                parent.lchild = new_node

            # insert the new node as a right child of one of the leaves
            elif (ch > parent.data):
                parent.rchild = new_node

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):

        # create an empty string to record the search sequence
        search_string = ''

        # handle case where character is the root of the tree
        if (ch == self.root.data):
            return '*'

        # traverse through the binary tree to find the character,
        # adding to the search string along the way
        current_node = self.root
        while (current_node != None) and (current_node.data != ch):

            if (ch < current_node.data):
                search_string += '<'
                current_node = current_node.lchild
            elif (ch > current_node.data):
                search_string += '>'
                current_node = current_node.rchild

        return search_string

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):

        # start the traversal at the root of the tree
        current_node = self.root

        # iterate through the string directions to find the character
        for ch in st:
            # handle case where the character is not in the tree
            if (current_node == None):
                return ''
            else:
                # go left
                if ch == '<':
                    current_node = current_node.lchild
                # go right
                if ch == '>':
                    current_node = current_node.rchild

        # return the found character
        return current_node.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):

        # convert the string to lowercase
        st.lower()

        # create an empty encrypted string
        encrypted_string = ''

        # traverse through the string, adding each alphabet character to the
        # encrypted string by using its search string
        for char in st:
            if ((ord(char) == 32) or (ord(char) >= 97 and ord(char) <= 122)):
                encrypted_string += self.search(char)
                encrypted_string += '!'

        # return the encrypted string
        return encrypted_string[:-1]

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):

        # create an empty decrypted string
        decrypted_string = ''

        # split the string with the given delimiter to get the directions
        # in the binary tree for each character
        directions = st.split('!')

        # add each character to the decrypted string by using its
        # direction string
        for direction in directions:
            decrypted_string += self.traverse(direction)

        # return the decrypted string
        return decrypted_string

def main():

    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print (the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print (the_tree.decrypt(str_to_decode))

if __name__ == "__main__":
    main()
