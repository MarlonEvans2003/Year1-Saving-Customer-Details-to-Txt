
def menuInput():
    print('*******************************')
    print('* select either 1 or 2        *')
    print('* 1: add new customer detail  *')
    print('* 2: view existing customer   *')
    print('*******************************')
    choice = int(input('select 1 or 2\n'))
    while choice != 1 and choice != 2:
        choice = input('You must either enter 1 or 2\n')
    return choice

import datetime
import random
#
#
#
def Firstname():
    firstname = input("Please enter your first name: ")
    while True:
        if firstname.isalpha() and len(firstname)>1 and len(firstname)<20:
            return firstname
            break
        else:
            firstname = input("Please enter your first name: ")


def Lastname():
    lastname = input("Please enter your last name: ")
    while True:
        if lastname.isalpha() and len(lastname)>1 and len(lastname)<20:
            return lastname
            break
        else:
            lastname = input("Please enter your last name: ")

def Birth():
    birth = input("please enter your date of birth as DD/MM/YYYY ")
    while True:  
        try:
           datetime.datetime.strptime(birth, '%d/%m/%Y')
        except ValueError:
            print("Please enter a valid date of birth: ")
            birth = input("please enter your date of birth as DD/MM/YYYY ")
        else:
            return birth
            break

def drivingYears():
    DrivingYears = int(input("Please enter the amount of years you have been driving: "))
    while True:
        if (DrivingYears)<16 and (DrivingYears) >0:
            return DrivingYears
            break
        else:
            DrivingYears = int(input("Please enter the amount of years you have been driving: "))

def UserGender():
    usergender = input("Please enter your Gender: ")
    usergender = usergender.upper()
    while True:
        if (usergender != "M") and (usergender != "F"):
            usergender = input("please enter your gender: ")
        else:
            return usergender
            break

def randomcustomernum():
    num = random.randint(100000,999999)
    return num


def findCustomer(AskNum):
    for line in open('Customers.txt',"r").readlines(): # Read the lines
        #global cust_info
        cust_info = line.split() # Split on the space, and store the results in a list of two strings
        if cust_info == None:    # EOF reached
            return[False]
        if AskNum == cust_info[0] :
            print("Customer found for id: "+ cust_info[0])
            return [True, cust_info[0], cust_info[1], cust_info[2], cust_info[3]]


choice = menuInput()
if choice == 1:
    # input customer details and validate ALL
    F = Firstname()
    L = Lastname()
    B = Birth()            
    D = drivingYears()
    G = UserGender()
    N = randomcustomernum()
    # write to file
    Total = (str(N) + " " + F + " " + L + " " + B + " " + str(D) + " " + G)
    with open("Customers.txt", "a") as f:
        f.write (Total)
        f.write ("\n")
    print("Details have been confirmed. Your customer id is: ",N)
elif choice == 2:
    AskNum = input("Please enter your customer ID: ")
    Find = findCustomer(AskNum) 
    if Find == None:
        print('customer not found') 
    else: 
        print('*******************************************')  
        print('**                                       **')
        print('**  customer id number : '+ Find[1] + '          **' ) 
        print('**  customer first name: '+ Find[2] )
        print('**  customer surname:    '+ Find[3] )
        print('**  customer DOB:        '+ Find[4] )
        print('**                                       **') 
        print('*******************************************')  
   