# On start
print("Welcome to prudent Health Care")

import time

#form
def writes(patient_id, first_name, last_name, address, gender, contact):
        fw = open('data2.txt', "a")
        fw.write("%1s%20s%20s%20s%20s%20s\n" % (patient_id, first_name, last_name, address, gender, contact))
        fw.close()

def last():
    print("Options:\n1=Register \n2=Login\n3=Appointment\n4=Accountant \n5=Exit")
    while True:
        option = input("> ")
        if option == "1":
            Register()
        elif option == "2":
            Login()
        elif option == "3":
            Appointment()
        elif option == "4":
            Accountant()
        elif option == "5":
            break
        else:
            print(option + " is not an option")




# login
def Login():
   pid=input("enter ur pid")
   users = open("data2.txt", 'r')

   for each_line in users:
       (patient_id, first_name, last_name, address, gender, contact) = each_line.split()

       if (patient_id == pid):
           print(patient_id, first_name, last_name, address, gender, contact)
   users.close()
   last()

def cash(pid, name, bill):
    fw = open('data1.txt', "a")
    fw.write("%1s%20s%20s\n" % (pid, name, bill))
    fw.close()


# registration
def Register():
    patient_id = input("Enter patient_id")
    first_name = input("Enter your first_name")
    last_name = input("Enter your last name")
    address = input("Enter your address")
    gender = input("Enter your gender ")
    contact = input("Enter your contact number")
    writes(patient_id, first_name, last_name, address, gender, contact)
    print("THANK YOU!!!")
    print("\nUser created!\n")
    last()

def appiontment(select_doctor):
    fw = open('data3.txt', "a")
    fw.write("%1s\n" % (select_doctor))
    fw.close()


def Appointment():
    print("Book an appointment")
    print("List of specialists")
    print("1. Doctor A")
    print("2. Doctor B")
    print("3. Doctor C")
    print("4. Doctor D")

    # This is for Doctor A
    select_doctor = input("Choose your doctor\n")

    if select_doctor == "1":

        print("Doctor A \n a. 08:00AM-09:00AM \n b.12:00AM-01:00PM \n c. 03:00PM-04:00PM")
        appiontment("Doctor A")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 08:00AM-09:00AM")
        elif your_time == "b":
            print("b. 12:00AM-01:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")

        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done.")
            last()
        else:
            print("waiting list")
            last()
            # This is for Doctor B

    elif select_doctor == "2":

        print("Doctor B \n a. 09:30AM-10:30AM\n b. 01:30PM-02:30PM \n c. 03:30PM-04:30PM")
        appiontment("Doctor B")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 09:30AM-10:30AM")
        elif your_time == "b":
            print("b. 01:30PM-02:30PM")
        elif your_time == "c":
            print("c. 03:30PM-04:30PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done.")
            last()
        else:
            print("waiting list")
            last()

            # This is for Doctor C

    elif select_doctor == "3":

        print("Doctor C \n a. 11:00AM-12:00AM \n b. 01:00PM-02:00PM \nc. 03:00PM-04:00PM")
        appiontment("Doctor C")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 11:00AM-12:00AM")
        elif your_time == "b":
            print("b. 01:00PM-02:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y\n")
        if notification == "y":
            print("y. Check up done.")
            last()
        else:
            print("waiting list")
            last()

            # This is for Doctor D

    elif select_doctor == "4":

        print("Doctor D \n a. 07:30AM-08:30AM \n b. 10:30AM-11:30AM \n c. 04:30PM-05:30PM")
        appiontment("Doctor D")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 07:30AM-08:30AM")
        elif your_time == "b":
            print("b. 10:30AM-11:30AM")
        elif your_time == "c":
            print("c. 04:30PM-05:30PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up Press y")
        if notification == "y":
            print("y. Check up done.")
            last()
        else:
            print("waiting list")
            last()

    else:
        print("Doctor is not available")
        last()

            # This is for payment process
def Accountant():
    pid = input("enter ur pid")
    users = open("data2.txt", 'r')

    for each_line in users:
        (patient_id, first_name, last_name, address, gender, contact) = each_line.split()

        if (patient_id == pid):
            print(patient_id, first_name, last_name, address, gender, contact)
    users.close()

    print("For cash Enter C")
    print("For credit Enter L")
    payment = input(">")
    if payment == "C":
        pid = input("Enter your patient_id: ")
        print("payment done by cash")
        name = input("Enter your name")
        bill = input("Please enter the receipt for the bill:-")
        print(bill)
        cash(pid, name, bill)
        print("Thank you")
        last()

    elif payment == "L":
        pid = input("Enter your patient_id: ")
        name = input("Enter your name: ")
        bill = input("Please enter the credit card number: ")
        print("payment done by credit")

        print(bill)
        cash(pid, name, bill)
        print("Thank you")
        last()
    else:
        print("not paid and go for payment")
        print("Thank You")
        last()

# ---When you open the program....
print("---------------------------------------")

print("Options:\n1=Register \n2=Login\n3=Appointment\n4=Accountant \n5=Exit")
while True:
    option = input("> ")
    if option == "1":
        Register()
    elif option == "2":
        Login()
    elif option=="3":
        Appointment()
    elif option == "4":
        Accountant()
    elif option == "5":
        break
    else:
        print(option + " is not an option")
print("-----------------------------------------")
# On exit
print("Shutting down...")
time.sleep(1)



