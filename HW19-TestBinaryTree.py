#  File: TestBinaryTree.py

#  Description: This program determines various characteristics of a binary tree such as whether it is
#               similar to another binary tree, the nodes at one of its levels, its height and the total
#               number of nodes in the tree.

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/13/2022

#  Date Last Modified: 11/14/2022


import sys
# Create the Node Class
class Node (object):
    # Initialize with attributes of data and the pointers to the left child and right child
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    # self.parent = None
    # self.visited = False

    # given code not used
    def __str__(self):
        string = str(self.data)
        return string

# Create the Tree class
class Tree(object):
    # Initialize with the root set to None
    def __init__(self):
        self.root = None
        # self.size = 0

    # insert data into the tree
    def insert(self, data):
        new_node = Node(data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # Define the is_similar method
    def is_similar(self, pNode):
        # self and pNode are both None, both trees are empty
        if (self.root == None) and (pNode.root == None):
            return True

        # self or pNode is None, one tree is empty
        elif (self.root == None) or (pNode.root == None):
            return False

        # evaluate both trees starting from root
        else:
            return self.similar_helper(self.root, pNode.root)

    def similar_helper(self, aNode, bNode):
        # base case: current nodes are empty, end of branch
        if (aNode == None) and (bNode == None):
            return True

        # one node is empty, either branches terminates
        elif (aNode == None) or (bNode == None):
            return False

        # proceed to evaluate both branches of both nodes if data matches
        elif (aNode.data == bNode.data):
            return self.similar_helper(aNode.lchild, bNode.lchild) \
                   and self.similar_helper(aNode.rchild, bNode.rchild)

        # data doesn't match between two nodes
        else:
            return False


    # Define the get_level helper. This needs the target level, current_level, a list, and the node passed in.
    def level_helper(self,target,current_level,lst, aNode):
        # the target is reached the current node is not empty, append it to the list
        if target == current_level and aNode != None:
                lst.append(aNode)

        # if the node is not empty, move down the tree by a level, to the left child or right child
        # recursively call the function
        elif aNode != None:
            self.level_helper(target,current_level+1,lst,aNode.lchild)
            self.level_helper(target,current_level+1,lst,aNode.rchild)



    def get_level (self, level):
        # Create an empty list
        lst = []
        target = level # Rename the desired level target
        aNode = self.root # initial node is the root
        current_level = 0 # initial level is 0

        # If the root is empty (empty tree), return an empty list
        if self.root == None:
            return []

        # call the recursive function
        self.level_helper(target,current_level,lst,aNode)

        # if the level does not exist, an empty list is returned
        return lst


    # Returns the height of the tree, operates using a list to append different levels.
    def height_helper(self,current_level, lst, aNode):
        # If the node is empty, append the level number of its parent (one level above it)
        if aNode == None:
            lst.append(current_level - 1)
        else:
            # Move down a level
            self.height_helper(current_level + 1, lst, aNode.lchild)
            self.height_helper(current_level + 1, lst, aNode.rchild)
    def get_height (self):
        lst2 = [] # Create an empty list
        aNode = self.root # initial node is the root
        current_level = 0 # initial level is the zeroth level
        self.height_helper(current_level,lst2,aNode) # call the recursive helper
        return max(lst2)+1 # retrieve the max of the list of levels

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root

    # Recursive helper to num_nodes
    def count_helper(self, aNode):
        # If the node is empty return 0
        if aNode == None:
            return 0
        else:
            # find all left counts, find all right counts, taking into account the root.
            # Increments one along the way
            left_count = self.count_helper(aNode.lchild)
            right_count = self.count_helper(aNode.rchild)
            return left_count + 1 + right_count
    def num_nodes (self):
        aNode = self.root # Initial node
        return self.count_helper(aNode) # return output of recursive helper

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    tree1 = Tree()
    for i in range(len(tree1_input)):
        tree1.insert(tree1_input[i])


    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints
    tree2 = Tree()
    for i in range(len(tree2_input)):
        tree2.insert(tree2_input[i])

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints
    tree3 = Tree()
    for i in range(len(tree3_input)):
        tree3.insert(tree3_input[i])

    # tree1.print_tree()
    # tree2.print_tree()
    # tree3.print_tree()

    # Test your method is_similar()
    # print(tree1.is_similar(tree3))
    # print(tree1.is_similar(tree2))


    # Print the various levels of two of the trees that are different
    # print(tree1.get_level(2))
    # print(tree1.get_level(3))

    # Get the height of the two trees that are different
    # Construct different trees of varying lengths and see the length of the longest 'chain'
    # print(tree1.get_height())



    # Get the total number of nodes a binary search tree
    # An integer should be returned. Different trees were set up of varying node numbers.
    # print(tree1.num_nodes())

if __name__ == "__main__":
  main()
