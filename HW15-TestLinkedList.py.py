#  File: TestLinkedList.py

#  Description: This program builds a linked list class with various functions.

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/30/2022

#  Date Last Modified: 10/31/2022


class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    # create a linked list
    # you may add other attributes
    def __init__ (self):
        self.first = None

    # get number of links 
    def get_num_links (self):

        current = self.first
        cnt = 0
        if (current == None):
            return cnt
        while (current != None):
            current = current.next
            cnt += 1
        return cnt        

    # add an item at the beginning of the list
    def insert_first (self, data): 
        newLink = Link (data)
        newLink.next = self.first
        self.first = newLink

    # add an item at the end of a list
    def insert_last (self, data): 
        newLink = Link (data)
        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next

        current.next = newLink

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order (self, data): 
        newLink = Link (data)
        current = self.first

        if (current == None):
            self.first = newLink
            return
        
        while (current.next != None and newLink.data > current.data):
            current = current.next

        newLink.next = current.next
        current.next = newLink


    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        current = self.first

        if (current == None):
            return None

        while (current.data < data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link (self, data):
        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
            current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        return ' '.join([str(node.data) for node in self])

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list (self):
        current = self.first
        newhead = Link (current.data)
        newList = LinkedList()
        newList.first = newhead

        if (current == None):
            return newList
        
        while (current.next != None):
            current = current.next
            newList.insert_last(current.data)
        
        return newList
       
    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list (self): 
        current = self.first
        newLink = Link (current.data)
        newList = LinkedList()
        newList.first = newLink

        if (current == None):
            return newList
        
        while (current.next != None):
            current = current.next
            newList.insert_in_order(current.data)
        
        return newList


    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list (self): 
        current = self.first
        newLink = Link (current.data)
        newList = LinkedList()
        newList.first = newLink

        if (current == None):
            return newList
        
        while (current.next != None):
            current = current.next
            newList.insert_first(current.data)
        
        return newList

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):

        current = self.first

        if (current == None):
            return False
        
        while (current.next != None and current.data < current.next.data):
            current = current.next

        if (current.next == None):
            return True
        else:
            return False


    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        return self.first == None

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list (self, other): 
        current = self.first
        current_other = other.first

        if (current == None and current_other == None):
            return LinkedList()

        elif(current != None):
            return self.copy_list()

        elif(current_other != None):
            return other.copy_list()  
        else:
            newList = LinkedList()
            while(current.data != None or current_other.data != None):
                if(current.data != None and current_other.data != None):
                    if (current.data > current_other.data):
                        newList.insert_last(current_other)
                        current_other = current_other.next
                    else:
                        newList.insert_last(current)
                        current = current.next
                elif(current.data != None):
                    newList.insert_last(current)
                    current = current.next  
                else:
                    newList.insert_last(current_other)
                    current_other = current_other.next  
        return newList                                  


    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        current = self.first
        current_other = other.first
        if (self.get_num_links() != other.get_num_links()):
            return False

        while(current.data != None):
            if current.data != current_other.data():
                return False
            current = current.next
            current_other = current_other.next
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates (self):
        current = self.first
        newList = LinkedList()
        if (current == None):
            return newList
        newLink = Link (current.data)
        newList.first = newLink

        while(current.next != None):
            current = current.next
            if  (newList.find_unordered(current.data) != None):    
                newList.insert_last(current.data)   

        return newList




def main():
    '''
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    my_list = LinkedList()
    my_list.insert_first(12)
    my_list.insert_first(11)
    my_list.insert_first(10)
    my_list.insert_first(9)
    my_list.insert_first(8)
    my_list.insert_first(7)
    my_list.insert_first(6)
    my_list.insert_first(4)
    my_list.insert_first(3)
    my_list.insert_first(2)
    my_list.insert_first(1)
    my_list.insert_first(0)
    my_list.insert_first(-1)
    my_list.insert_first(-2)
    # print(my_list)

    # Test method insert_last()
    my_list.insert_last(13)
    # print(my_list)

    # Test method insert_in_order()
    my_list.insert_in_order(5)
    # print(my_list)

    # Test method get_num_links()
    num_links = my_list.get_num_links()
    # print(num_links)

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    result1 = my_list.find_unordered(7)
    result2 = my_list.find_unordered(14)
    # print(result1, result2)

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    result3 = my_list.find_ordered(7)
    result4 = my_list.find_ordered(14)
    # print(result3, result4)

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    result5 = my_list.delete_link(13)
    result6 = my_list.delete_link(15)
    # print(result5, result6)
    # print(my_list)

    # Test method copy_list()
    copied_list = my_list.copy_list()
    # print(copied_list)

    # Test method reverse_list()
    reversed_list = my_list.reverse_list()
    # print(reversed_list)

    # Test method sort_list()
    unsorted_list = LinkedList()
    unsorted_list.insert_first(1)
    unsorted_list.insert_first(2)
    unsorted_list.insert_first(3)
    # print(unsorted_list)
    sorted_list = unsorted_list.sort_list()
    # print(sorted_list)

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    result7 = my_list.is_sorted()
    result8 = unsorted_list.is_sorted()
    # print(result7, result8)

    # Test method is_empty()
    empty_list = LinkedList()
    result9 = my_list.is_empty()
    result10 = empty_list.is_empty()
    # print(result9, result10)

    # Test method merge_list()
    merged_list = my_list.merge_list(sorted_list)
    # print(merged_list)

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    duplicate_list = LinkedList()
    duplicate_list.insert_first(3)
    duplicate_list.insert_first(2)
    duplicate_list.insert_first(1)
    result11 = my_list.is_equal(sorted_list)
    result12 = sorted_list.is_equal(duplicate_list)
    # print(result11, result12)

    # Test remove_duplicates()
    clean_list = merged_list.remove_duplicates()
    print(clean_list)
    '''

if __name__ == "__main__":
    main()