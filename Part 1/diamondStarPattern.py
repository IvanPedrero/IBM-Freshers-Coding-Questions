"""

Given 'r' rows, print the following figure:

r = 5

  * 
 * * 
* * * 
 * * 
  * 

"""


def diamondStarPatternInverted(r):

    # Maximum width of the diamond.
    maxWidth = int(r/2)

    # Used for the diagonal size.
    leftSpace = maxWidth

    # Stars per row.
    starPerRow = 1

    isPair = False

    # Normalize the diamond size if the number of rows is pair.
    if r % 2 == 0:
        isPair = True
        r += 1

    for i in range(r):

        # Define the line.
        line = (leftSpace * " ") + (starPerRow * "* ")

        # Crescent stars.
        if i < maxWidth:
            leftSpace -= 1
            starPerRow += 1
        # Decreasing stars.
        else:
            leftSpace += 1
            starPerRow -= 1

        # Don't print the middle line if pair, as the diamond will not get printed.
        if i == maxWidth and isPair:
            continue

        # Print the line.
        print(line)


# Driver code.
if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        diamondStarPatternInverted(r)
