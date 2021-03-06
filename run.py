#!/usr/bin/env python3.8
from lock import Credentials
from lock import User
import string,random,time


def new_account(id,user_name,password):
    '''
    Function to creating new account
    '''
    new_user = Credentials(id,user_name,password)
    return new_user

def create_user(user):
    '''
    Function that creates the user account
    '''
    user.create_account()

def authenticate(username,keypin):
    '''
    Function responsible for signing in
    '''
    return Credentials.authenticate_account(username,keypin)

def my_new_data(user_id,data_id,website,weblogin,name):
    '''
    Function that creates new data for storing password
    '''
    new_data = User(user_id,data_id,website,weblogin,name)
    return new_data

def save_data(data):
    '''
    Function that saves the new data created
    '''
    data.save_password()

def display_data(data,number):
    '''
    Function that displays the user data
    '''
    return User.display_data(data,number)

def data_existing(data):
    '''
    Function that checks if user data exists
    '''
    return User.existing_data(data)

def password_generator(count):
    '''
    Function that generates a password
    '''
    pass_list=[]
    round = 1
    while round<=count:
        gen_password = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase )
        pass_list.append(gen_password)
        round+=1
    return ''.join(pass_list)

def main():

    print("This is your password locker, What is your name please?")
    name = input()

    the_id =0
    entries = []
    print("\n" + f"Welcome to password Locker  {name}")
    print("-"*40)
    while True:
        print("Type:\n  cc to create a new account\n  ss to sign in to existing \n  ex to exit")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create account to continue:"+"\n"+"-"*25 + " \n Enter Username:")
            name1 = input("New Username: ")
            print(" Enter password:")
            key1 = input("New Password: ")

            print("\n")
            create_user(new_account(the_id,name1,key1,))
            the_id+=1
            print(f"User {name1} has been created.\n Please sign in to continue")
            entries.append(0)
            print("-"*27)


        elif short_code == "ss".lower():
            print("Enter username and password to continue:")
            print("-"*40)
            login = input("Username: ")
            key2 = input("Password: ")
            results = authenticate(login,key2)
            if results == 0:
                print("\n")
                print("Invalid username and/or password")
                print("-"*27)
            elif results!=0:
                print("\n")
                print(f"Welcome {results.user_name}! What would you like to do?")
                while True:
                    print("Type:\n  gn - generate random password\n vp - View Passwords \n  lo - Log Out")
                    short_code1 = input().lower()
                    if short_code1 == "gn":
                        print("Add a website and create password for security:")
                        print("Enter Website>")
                        thewebsite = input()
                        print("Enter Username>")
                        thename = input()
                        print("Input the length of the password")
                        password_length = int(input("Password length> "))
                        thewebkey = password_generator(password_length)
                        my_identity = results.identify
                        save_data(my_new_data(my_identity,entries[my_identity],thewebsite,thewebkey,thename))
                        entries[my_identity]=entries[my_identity]+1
                        print("\n Please wait...")
                        time.sleep(2.0)
                        print("\n")
                        print(f"Your {thewebsite} is {thename} and password is {thewebkey}")
                        print("-"*45)

                    elif short_code1 == "vp":
                        if data_existing(results.identify):
                            store = entries[results.identify]
                            print(f"You have {store} passwords:")
                            print("\n")
                            thedata=0
                            while thedata < store:
                                thepassword = display_data(results.identify,thedata)
                                print(f"{thedata+1}. {thepassword.website} ---- {thepassword.web_key}")
                                thedata+=1
                            print("\nEnter a command to continue")
                            print("-"*20)
                        else:
                            print("\nYou have no data.\nType ad to generate some passwords")
                            print("-"*20)


                    elif short_code1 == "lo":
                        print("\n")
                        print(f"Goodbye {results.user_name}!")
                        print("-"*30)
                        break
                    elif short_code1 == "gn":
                        print("Add a website and create password for security:")
                        print("Enter Website:")
                        thewebsite = input()
                        print("Enter Username:")
                        thename = input()
                        print("Enter Password")
                        thewebkey = input()
                        my_identity = results.identify
                        save_data(my_new_data(my_identity,entries[my_identity],thewebsite,thewebkey,thename))
                        entries[my_identity]=entries[my_identity]+1
                        print("\nWait...")
                        time.sleep(1.5)
                        print("\n")
                        print(f"Your {thewebsite} username is {thename} and password is {thewebkey}")
                        print("-"*45)
                        
                  
                    else:
                        print("Invalid entry. Enter command again")
                        print("\n"+"-"*40)

        elif short_code == "ex":
            print("\n")
            print(f"Logged off")
            break
        else:
            print("Invalid entry. Enter command again")
            print("\n"+"-"*40)


if __name__ == '__main__':
    main()