#  File: Poly.py

#  Description:

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/03/2022

#  Date Last Modified: 11/04/2022



import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    new_link = Link(coeff,exp)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None and new_link.exp > current.exp):
      current = current.next
    #if (new_link.exp == current.exp and new_link.coeff == current.coeff )
    current.next = new_link    

  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
      current = self.first
      newhead = Link (current.coeff,current.exp)
      newList = LinkedList()
      newList.first = newhead

      if (current == None):
          return newList
      
      while (current.next != None):
          current = current.next
          newList.insert_in_order(current.coeff,current.exp)
      
      return newList


    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
  def delete_link (self, coeff, exp):
      current = self.first
      previous = self.first

      if (current == None):
          return None

      while (current.coeff != coeff and current.exp != exp):
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

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    current = self.first
    current_other = p.first

    if (current == None and current_other == None):
        return LinkedList()

    elif(current != None):
        return self.copy_list()

    elif(current_other != None):
        return p.copy_list()  
    else:
        newList = LinkedList()
        while(current.coeff != None or current_other.coeff != None):
            if(current.coeff != None and current_other.coeff != None):
                if (current.exp > current_other.exp):
                    newList.insert_in_order(current.coeff,current.exp)
                    current_other = current_other.next
                elif (current.exp < current_other.exp):
                    newList.insert_in_order(current.coeff,current_other.exp)
                    current = current.next
                else:
                    newList.insert_in_order(current.coeff+current_other.coeff,current.exp)
                    current = current.next                  
            elif(current.coeff != None):
                newList.insert_in_order(current.coeff,current.exp)
                current = current.next  
            else:
                newList.insert_in_order(current_other.coeff,current_other.exp)
                current_other = current_other.next  
    return newList   

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):

    current = self.first
    current_other = p.first

    if (current == None and current_other == None):
        return LinkedList()

    elif(current != None):
        return self.copy_list()

    elif(current_other != None):
        return p.copy_list()  
    else:
        newList = LinkedList()
        while(current.coeff != None):
          while(current_other.coeff != None):
            newList.insert_in_order(current.coeff*current_other.coeff,current.exp+current_other.exp) 
            current_other = current_other.next  
          current = current.next
    
    current = newList.first
    current_next = current.next
    while(current != None):
      while(current_next != None):
        if(current.exp == current_next.exp):
          current.coeff += current_next
          tmp = current_next.next
          newList.delete_link(current_next.coeff,current_next.exp)
          current_next = tmp
        current = current.next 
    return newList  

  # create a string representation of the polynomial
  def __str__ (self):
    # create a new string
    poly_string = ''

    # add the first expression to the string
    current = self.first
    if (current.coeff != 0):
      poly_string = str(current)
    current = current.next

    # add subsequent expressions to the string
    while (current != None):
      if (current.coeff != 0):
        poly_string += ' + ' + str(current)
      current = current.next

    return poly_string

def main():
  # read data from file poly.in from stdin
  terms = int(sys.stdin.readline().strip())

  # create polynomial p
  poly_p = LinkedList()
  for i in range(terms):
    line = sys.stdin.readline().strip()
    numbers = line.split()
    poly_p.insert_in_order(int(numbers[0]), int(numbers[1]))

  #print('Polynomial 1:', poly_p)

  sys.stdin.readline()

  # read data from file poly.in from stdin
  terms = int(sys.stdin.readline().strip())

  # create polynomial q
  poly_q = LinkedList()
  for i in range(terms):
    line = sys.stdin.readline().strip()
    numbers = line.split()
    poly_q.insert_in_order(int(numbers[0]), int(numbers[1]))

  #print('Polynomial 2:', poly_q)

  # get sum of p and q and print sum
  poly_sum = poly_q.add(poly_p)
  print(poly_sum)

  # get product of p and q and print product
  mult_sum = poly_q.mult(poly_p)
  print(mult_sum)

if __name__ == "__main__":
  main()