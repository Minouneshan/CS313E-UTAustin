# File: ExpressionTree.py

# Description: 

#  File: ExpressionTree.py

#  Description: Binary tree data strcuture to evaluate expressions

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/06/2022

#  Date Last Modified: 11/06/2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):

        # create a node for self.root, and set current to self.root        
        current_node = Node()
        self.root = current_node

        # create a stack object        
        stack = Stack()  
        # create a list of tokens out of expression
        tokens = expr.split()

        for token in tokens:
            # token is left parenthesis
            if token == '(':
                current_node.lChild = Node()
                stack.push(current_node)
                current_node = current_node.lChild

            # token is an operator
            elif token in operators:
                current_node.data = token
                stack.push(current_node)
                current_node.rChild = Node()
                current_node = current_node.rChild

            # token is right parenthesis                
            elif token == ')':
                if not stack.is_empty():
                    current_node = stack.pop()

            # token is a number
            else:
                current_node.data = token
                current_node = stack.pop()
                    

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # current node is a leaf node, meaning it is an operand
        if (aNode.lChild == None) and (aNode.rChild == None):
            return aNode.data
        
        # current node has children, meaning it is an operator
        else:
            # evaluate left and right children, recursively
            token_1 = str(self.evaluate(aNode.lChild))
            token_2 = str(self.evaluate(aNode.rChild))
            operator = aNode.data

            expr = token_1 + operator + token_2

            return float(eval(expr))
        


    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        # return a string using recursion; traversing center, left, right
        if (aNode != None):
            string = aNode.data + ' ' + self.pre_order(aNode.lChild) + self.pre_order(aNode.rChild)
            return string
        return ''

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        # return a string using recursion; traversing left, right, center
        if (aNode != None):
            string = self.post_order(aNode.lChild) + self.post_order(aNode.rChild) + ' ' + aNode.data
            return string
        return ''

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
