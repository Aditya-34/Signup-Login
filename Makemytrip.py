import random #module to generate random numbers
from time import sleep #module to add delay in the program

credentials = {}

def otp():
    user_otp = random.randint(1000,9999) #generate a random 4 digit number
    return user_otp

def login():
    username = input("Enter your username:")
    password = input("Enter your password:")
    if username in credentials:
        if credentials[username] == password:
            print("login Successfully")
        else:
            print("Invalid Password")
    else:
        print("Invalid USername:")

def signup():
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")
    emil_id = input("Enter your email id:")
    Phone_no = input("Enter your phone number:")
    username = input("Enter your username:")
    password = input("Enter your password:")
    confirmpassword = input("Confirm your password:")
    if password == confirmpassword:
        credentials[username] = password
        o = otp()
        print("Generated OTP......")
        sleep(3)
        print("Your OTP is:",o)
        u_otp = int(input("Enter the OTP:"))
        if o == u_otp:
            print("Account created successfully!!!")
        else:
            print("OTP mismatch. Please try again.")
    else:
        print("Password and confirm password do not match. Please try again.")

def main():
    print("Welcome to Simple Signup/Login of MakeMyTrip")
    while True:
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Enter your choice:")
        if choice == '1':
            login()
        elif choice == '2':
            signup()
        elif choice == '3':
            print("Thank you for using MakeMyTrip. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")  
main()   
    