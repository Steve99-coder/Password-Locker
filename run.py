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
