"""

Given 'r' rows, print the following figure:

r = 5

*****
 *****
  *****
   *****
    *****

"""


def rhombusStarPatter(r):
    
    # Used for the diagonal printing.
    leftSpace = 0
    
    # For each row...
    for i in range(r):

        # Print the number of cumulative left spaces plus the row of stars.
        line = (leftSpace * " ") + (r * "*")

        # Add to the growing left space.
        leftSpace += 1

        # Print the line.
        print(line)


# Driver code.
if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        rhombusStarPatter(r)