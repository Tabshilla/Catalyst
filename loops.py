#loops repeatedly do something until the condition is false 

#below we are looping; iteration of values in a list of numbers

def loop1():
    list = [10, 20,30,40,50]
    for item in list:
        print(item)
loop1()

def loop2():
    for i in range(10):
        print(i)
        item = 1
loop2()

def loop3():
    for item in range(1,10): #1 represents the start and 10 represents the end
        print(item)
        
        if item % 2==0:
            print(item)
loop3()




def loop5():
        #from line 15 to line 17 is a block of code. a block of code is a collection of related statements
        #a block of code is identified by identation
    for i in range(1,20):
        if i % 2==1:
             print(i)
loop5()

digits = [23,67,50,70,89]
def loop6():
    for i in digits:
        print(i)
    else:
        print("no more digits")
loop6()

def loop7():
    for i in range(1,20):
        if i % 2!=0:
            print(i)
    else:
        print("no items left")
loop7()



       
       
       
       
       
       
       
        #while loop



    