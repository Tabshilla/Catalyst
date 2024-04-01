def tests(test1, test2):
    # This function compares the marks of two tests and returns the higher mark.
    if test1 == test2:  # If test1 mark is equal to test2 mark
        return test1  # Return test1 mark
    else:
        return test2  # Otherwise, return test2 mark

# Take input for test two marks from the user
test2 = int(input('Please enter Marks for test two: '))

# Define the courseWrk function
def courseWrk(cswork):
    # This function calculates the final coursework marks.

    # Call the tests function to get the higher mark between test1 and test2
    # Note: test1 is not defined here, so it needs to be defined before calling courseWrk function
    # Assuming test1 is provided as a global variable or defined elsewhere
    testsMark = tests(test1, test2)

    # Calculate the average of coursework marks and tests marks
    avgtestsCswork = (cswork + testsMark) / 2

    # Calculate the final coursework marks by considering 40% weightage of the average
    fnltestsCswork = avgtestsCswork * (40 / 100)

    # Print separator
    print('..............................')

    # Print the final coursework marks
    print('Your final coursework marks is:', fnltestsCswork)
    print('..............................')

# Take input for coursework marks from the user
cswork = int(input('Please enter your coursework Marks: '))

# Call the courseWrk function with the coursework marks provided by the user
courseWrk(cswork)
