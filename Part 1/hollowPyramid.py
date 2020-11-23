"""

Given 'r' rows, print the following figure:

r = 5

    *
   *  *
  *    *
 *      *
**********

"""


def hollowPyramid(r):

    # Used for the diagonal.
    leftSpace = r - 1

    # Used for the hollow space in the middle.
    middleSpace = 0

    # Used for the base.
    baseLen = r*2

    # For each level of the pyramid...
    for i in range(r-1):

        # The first level will have only one star, the rest will have two.
        if i == 0:
            line = (leftSpace * " ") + "*"
        else:
            line = (leftSpace * " ") + "*" + (middleSpace * " ") + "*"
        
        # Add one to the left space and add two to the middle space, so the pyramid can be formed.
        leftSpace -= 1
        middleSpace += 2
        
        # Print the line
        print(line)

    # Print the base.
    print(baseLen * "*")


# Driver code.
if __name__ == "__main__":
    
    r = int(input("Enter the number of rows : "))

    if r != None :
        hollowPyramid(r)