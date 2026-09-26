# ----------------------------------------------
#        Name: Ash Rulifson
#       Peers: (add any collaborators)
#  References: Textbook (How to Think Like a Computer Scientist)
# ----------------------------------------------

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """return user inputted integers"""
    x = int(input("give me x: ")) # get user's inputs and make them integers
    y = int(input("give me y: "))
    return x,y

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a,b):
    """calculate and show steps to divide a product by a sum of the same numbers"""
    abproduct = a*b
    print(f"mult result: {abproduct}")
    absum = a+b
    print(f"add result: {absum}")
    print(" ") # blank line for readability
    ab_multadd = (abproduct/absum)
    return ab_multadd 

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """print the inputs and calculations in an easy-to-read format"""
    print("****************")
    print("RESULTS:")
    print(f"first number: {a}")
    print("second number:",b) 
    print("multadd result:",ab_multadd)
    print("================")

def main ():
    """run all previously defined functions in the right order and with context"""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  store the returned values into two variables: x and y
    x, y=read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x and y you obtained above;
    #  store the returned value in a variable called xy_multadd
    xy_multadd = compute_multadd(x,y) # defining this as output of compute_multadd

    # Task 3.2:
    #  Complete the line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
    print_fancy(x,y,xy_multadd) # call print_fancy with arguments previously defined

    print(" ") # blank line for readability

    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
