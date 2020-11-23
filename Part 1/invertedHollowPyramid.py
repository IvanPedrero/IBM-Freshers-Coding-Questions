"""

Given 'r' rows, print the following figure:

r = 5

**********
 *      *
  *    *
   *  *
    *

"""


def invertedHollowPyramid(r):

    # Used for the diagonal pattern.
    backSpace = 1

    # Used for the hollow space in the middle.
    middleSpace = (r*2 - 4)

    # Used to print the base of the pyramid.
    baseLen = r*2

    # Print the base.
    print(baseLen * "*")

    # For each level of the pyramid...
    for i in range(1, r):

        # The last level of the piramid, only have one star.
        if i == r-1:
            line = (backSpace * " ") + "*"
        # All the other levels, have two stars separated by hollow space.
        else:
            line = (backSpace * " ") + "*" + (middleSpace * " ") + "*"

        # Add one to the left space for the diagonal.
        backSpace += 1

        # Remove two spaces for the hollow space.
        middleSpace -= 2

        # Print the line.
        print(line)


# Driver code.
if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        invertedHollowPyramid(r)
