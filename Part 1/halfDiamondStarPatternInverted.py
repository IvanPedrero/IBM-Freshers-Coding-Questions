"""

Given 'r' rows, print the following figure:

r = 5

  *
 **
***
 **
  *

"""
import math


def halfDiamondStarPatternInverted(r):

    # Maximum width of the diamond.
    maxWidth = math.ceil(r/2)

    # Used for the diagonal size.
    leftSpace = maxWidth - 1

    # Stars per row.
    starPerRow = 1

    isPair = False

    # Normalize the diamond size if the number of rows is pair.
    if r % 2 == 0:
        isPair = True
        r += 1
        maxWidth += 1
        leftSpace += 1

    for i in range(r):

        line = (leftSpace * " ") + (starPerRow * "*")

        if i < maxWidth - 1:
            leftSpace -= 1
            starPerRow += 1
        else:
            leftSpace += 1
            starPerRow -= 1

        # Don't print the middle line if pair, as the diamond will not get printed.
        if i == maxWidth and isPair:
            continue

        print(line)


# Driver code.
if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        halfDiamondStarPatternInverted(r)
