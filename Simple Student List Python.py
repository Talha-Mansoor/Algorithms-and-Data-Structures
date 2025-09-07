# Name: Talha Mansoor
# NSID= kgy284
#Student number: 11346490
# Instructor's name: Ed Pakroka

students = []
register = []

def create_list():
    global students
    students = [ ("Chika Fujiwara" , 16 , True) , ("Ahmed Amjad Dar" , 7 , False) ,("Makise Kurise" , 2 , True) ,
                 ("Tony Stark" , 54 , True),("Darth Sidius" , 66 , False), ("Jack Sparrow" , 27 , False) ]

'''Defining creat_list function to create list. 
Defining reg_student function to register students. by asking for name, student number and AES choice'''

def reg_student (students):
    global register
    students = [ ("Chika Fujiwara" , 16 , True) , ("Ahmed Amjad Dar" , 7 , False) ,("Makise Kurise" , 2 , True) ,
                 ("Tony Stark" , 54 , True),("Darth Sidius" , 66 , False), ("Jack Sparrow" , 27 , False) ]
    name = str(input("Enter Student Name: "))

    number = int(input("Enter Student Number: "))
    AES = str(input("Do you need AES accommodation (Y/N): "))
    for j in AES:
        if (j == "Y" or j == "y" or j == "N" or j == "n"):                    #giving options for AES
            if (j == "n" or j == "N"):
                register+= [(name, number, False)]
                students.extend(register)
                print(students)
            if (j == "y" or j == "Y"):
                register+= [(name, number, True)]
                students.extend(register)
                print(students)


'''defining function to delete student info'''
def delete(number):
    global students
    create_list()
    number = int(input("Please enter your Student Number: "))

    for i in range(len(students)):                              #check list with that number and delete it
        if students[i][1] == number:
            print(students[i][0])
            del students[i]
            print("Student number", number, "has been unregistered.")
            print(students)


            break
'''defining function to print list'''
def printinfo(students):
    create_list()
    print ("Student list: "+"\n")
    for i in range (len(students)):
        print(students[i][0] , "|" ,students[i][1] , "|" , students[i][2], "\n" )
''''defining function for user interface'''
def choice():
    print()
    global response
    while True:
        try:
            response = int((input("Please choose an option:\n"                 #Displaying options and taking in input
            
              "1. Create student list\n"
              "2. Register a student\n"
              "3. Unregister a student\n"
              "4. Display student information\n"
              "5. Quit\n"
              "Your choice is: ")))
            x = isinstance(response, int)

            #ask user to input the choice
            if 1<= response <= 5 :
                return (int(response))


            else:
                print("Invalid response. Please only enter a single number:")
        except ValueError:
            print("Provide an integer value...")
            continue

choice()
while response in range(1,6):                            #Depending upon response running different functions accordingly
    try:
        if response == 1:
            create_list()
            for i in students:
                print(i)
                print()

        elif response == 2:
            reg_student(students)


        elif response == 3:
            delete(students)

        elif response == 4:
            create_list()
            printinfo(students)

        elif response == 5:
            print("Thank you. Have a good day!")
            exit()
        choice()
    except ValueError:
        print("Provide an integer value For number")



