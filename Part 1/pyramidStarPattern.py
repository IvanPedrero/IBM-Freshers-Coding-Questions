"""

Given 'r' rows, print the following figure:

r = 5

    *
   ***
  *****
 *******
*********

"""

def pyramidStarPattern(r):

    maxWidth = r*2

    leftSpace = r - 1
    starsPerRow = 1


    for i in range(r):
        
        line = (leftSpace * " ") + ( starsPerRow * "*")

        leftSpace -= 1
        starsPerRow += 2

        print(line)


# Driver code.
if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        pyramidStarPattern(r)