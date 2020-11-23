"""

Given 'r' rows, print the following figure:

r = 5

*********
 *******
  *****
   ***
    *

"""

def invertedPyramidStarPattern(r):


    starsPerRow = r * 2 - 1

    leftSpace = 0

    for i in range(r):
        line = (leftSpace * " ") + (starsPerRow * "*")

        leftSpace += 1
        starsPerRow -= 2

        print(line)

# Driver code.
if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        invertedPyramidStarPattern(r)