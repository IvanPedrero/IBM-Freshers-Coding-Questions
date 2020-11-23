"""

Given 'r' rows, print the following figure:

r = 5

*****
*****
*****
*****
*****

"""


def squareStarPattern(r):

    # For each row...
    for i in range(r):
        # Print the same number of stars from the height.
        print(r*"*")


# Driver code.
if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        squareStarPattern(r)
