
#  File: Triangle.py

# Description: This program finds the greatest sum path, using only adjacent values, through a triangle of integers.
#              It uses 4 different algorithms to solve the problem: exhaustive search (recursion), greedy search,
#              divide and conquer (recursion) and dynamic programming.


#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/07/2022

#  Date Last Modified: 10/10/2022

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    # Initialize a variable to calculate each individual route and a list which stores all routes
    route = 0
    routes_list = []

    # Call the helper function to check all possible paths, starting with the first row and first column
    row = 0
    col = 0
    brute_force_calculator(grid, row, col, route, routes_list)

    # Return the route with the highest value from the list of all route values
    maximum_sum = max(routes_list)
    return maximum_sum

def brute_force_calculator(grid, row, col, route, routes_list):

    # When the route has reached the end of the triangle, adds the route to the root list
    if (row == len(grid)):
        routes_list.append(route)

    # If the end of the triangle has not been reached, the number in question is appended to the route
    # Then, the function is called twice for the two adjacent values in the next row that need to be
    # added to their respective routes
    else:
        route += grid[row][col]
        next_row = row + 1
        next_col = col + 1
        return brute_force_calculator(grid, next_row, col, route, routes_list) or \
               brute_force_calculator(grid, next_row, next_col, route, routes_list)

# returns the greatest path sum using greedy approach
def greedy (grid):

    # Create a list to store the route value from each row
    route = []

    # Add the value from the top of the triangle to the list
    route.append(grid[0][0])

    # Goes through each row and adds the larger of the two
    # adjacent values to the route
    col = 0
    for row in range(1, len(grid)):
        if (grid[row][col] > grid[row][col + 1]):
            route.append(grid[row][col])
        else:
            route.append(grid[row][col + 1])
            col = col + 1

    # Returns the sum of the route list
    route_sum = sum(route)
    return route_sum
# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):

    # Initialize a variable to store the highest value route and call the helper function,
    # starting with the first row and first column
    route = 0
    row = 0
    col = 0
    max_route = dac_helper(grid, row, col, route)

    # Return the route with the highest value route
    return max_route

def dac_helper(grid, row, col, route):

    # Return the route when it has reached the end of the triangle
    if (row == len(grid)):
        return route

    # If the end of the triangle has not been reached, add the current position to the route
    # Then, determine which of the two adjacent values in the next row results has a higher
    # valued route, pick it and add it to the current route
    else:
        route += grid[row][col]
        next_row = row + 1
        next_col = col + 1
        return max(dac_helper(grid, next_row, col, route), dac_helper(grid, next_row, next_col, route))
# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):

    # Duplicate the grid and reverse it to start the addition from the bottom
    my_grid = [row[:] for row in grid]
    my_grid = my_grid[::-1]

    # For each value in the grid starting from the second row, check if the value
    # directly beneath it or the value beneath it and one to the right is larger
    # Take the larger of the two values and add it to the current value
    for row in range(1, len(my_grid)):
        for col in range(len(my_grid[row]) - 1):
            if my_grid[row - 1][col] > my_grid[row - 1][col + 1]:
                my_grid[row][col] = my_grid[row - 1][col] + my_grid[row][col]
            else:
                my_grid[row][col] = my_grid[row - 1][col + 1] + my_grid[row][col]

    # The largest value will be the at the top of the triangle, which is now
    # the first value in the last row since the grid was reversed
    return my_grid[-1][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()

