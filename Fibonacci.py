# Name: Talha Mansoor
# NSID= kgy284
#Student number: 11346490
# Instructor's name: Ed Pakroka


'''Asking for input integer k in a while loop'''
while True:
    try:
        k=int(input("ENTER number of fibonacci terms you want dsiplayed (whole number):"))
    except ValueError:
        print("Invalid entry. please try again ")
        continue
    else:
        break
'''Terminating program for Negative input'''
if k<0:
    print("NEGATIVE value, program terminated")




'''Defining the Fucntion print_fib.
If input is zero then it asks again for input, initializing x, y and Fib to calculate fibonacci sequence'''
while k>=0:
    def print_fib(n):
        global Fib
        if n==0:
            return print("Fibonacci sequence terms do not exist in this amount. Please enter a positive Integer. ")

        x=0
        y=1
        Fib= []
        for i in range(n+1):
            Fib.append(x)
            x,y=y,x+y
        return print(Fib)

    print_fib(k)
    while True:
        try:
            k = int(input("ENTER number of fibonacci terms you want dsiplayed (whole number):"))
        except ValueError:
            print("Invalid entry. please try again ")
            continue
        else:
            break

'''If input is positive then it gives us the answer and asks again until a negative integer is inputted.'''