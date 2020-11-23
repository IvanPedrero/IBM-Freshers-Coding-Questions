"""

Given 'r' rows, print the following figure:

r = 5

*****
*   *
*   *
*   *
*****

"""



def hollowSquareStarPattern(r):
    
    # The middle range will be always the size of the row minus the left and right star.
    middleSpace = r - 2

    # For each row...
    for i in range(r):

        # If it's the top or the bottom, print the hole star line.
        if i == 0 or i == r - 1:
            line = "*" * r
        # Print the hollow part otherwise.
        else:
            line = "*" + (middleSpace * " ") + "*"

        # Print the line.
        print(line)


# Driver code.
if __name__ == "__main__":

    r = int(input("Enter the number of rows : "))

    if r != None:
        hollowSquareStarPattern(r)
