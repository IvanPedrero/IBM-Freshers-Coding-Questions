"""

Given 'r' rows, print the following figure:

r = 5

*
**
***
****
*****

"""

def rightTriangleStarPattern(r):
    
    # For all the rows...
    for i in range(1, r + 1):

        # Print the multiplied number of stars.
        print( i * "*")


# Driver code.
if __name__ == "__main__":
    
    r = int(input("Enter the number of rows : "))

    if r != None :
        rightTriangleStarPattern(r)