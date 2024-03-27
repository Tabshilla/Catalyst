def tests(test1, test2):
    #.defining a function tests and assigned parameters test1, test2.this is a conditional statement that compares values test1 and test2 to check if test1 is equal to test2
    if test1 == test2:
        #return test1 mark
        return test1
    else:
        #or return test2 mark if the marks are not the same
        return test2
#this prompts the user to enter the marks of test 2 and will be kept in variable2

test2 = int(input('Please enter Marks for test two: '))

'''
creating a global variable
test one was not defined, so it needs to be defined and it can be defined by declaring it as a global variable.

'''
def courseWrk(cswork):
    #defined a function called coursework
    testsMark = tests(test1,test2)
    #returned the variable tests(test1,test2)
    avgtestsCswork = (cswork + testsMark)/2
    #average coursework is calcualted as sum of cswok and testmark divide by 2
    fnltestsCswork = avgtestsCswork * (40/100)
    #output will be a 
    print('..............................')
    #output in the terminal and prints the final marks
    print('your final coursework marks is: ', fnltestsCswork)
    print('..............................')
#here we prompt the user to enter their coursework marks
cswork = int(input('Please enter your course work Marks: '))
#ivoke the function coursework with the argument cswork
courseWrk(cswork)