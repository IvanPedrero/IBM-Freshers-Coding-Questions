"""

Given the width 'w' and height 'h', print the following figure:

h = 6
w = 5

*****
*****
*****
*****
*****
*****

"""



def rectangleStarPattern(w, h):

    # For each row...
    for i in range(h):
        # Print the full row with the width.
        print(w * "*")
    

# Driver code.
if __name__ == "__main__":

    h = int(input("Enter the number of rows : "))
    w = int(input("Enter the number of cols : "))

    if h != None and w != None:
        rectangleStarPattern(w, h)
    
