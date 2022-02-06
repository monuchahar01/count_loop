#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 15:52:34 2022

@author: monu
"""

import pyrebase
import time

def insert_DB():
    
    start_time = time.time()
    print('Runnning in a insert_DB function\n')
    file1 = open("data.txt","r")  
    number = file1.read() 
    file1.close() 
    print('your running number is {}'.format(int(number)))
    print('time is {}'.format(start_time) )
    
    # Set the configuration for your app
    # TODO: Replace with your project's config object
    config = {
        "apiKey": "AIzaSyB2XIejSTMHpJ0zPH6I9nZvTl7jietPIyQ",
        "authDomain": "sample-75466.firebaseapp.com",
        "databaseURL": "https://sample-75466-default-rtdb.firebaseio.com",
        "projectId": "sample-75466",
        "storageBucket": "sample-75466.appspot.com",
        "messagingSenderId": "884351530348",
        "appId": "1:884351530348:web:b73cd083b908edf1702f49",
        "measurementId": "G-DZWS64021W"
    }
    firebase = pyrebase.initialize_app(config)
    
    # Get a reference to the database service
    db = firebase.database()
    
    # Try pushing some sample data
    sample = {'run_id':int(number),'time':start_time}
    #sample["Project"] = "Scrapper"
    db.child("Testing").set(sample)
    
    file1 = open("data.txt","w")
    number=str(int(number)+1)
    if number == '11':
        number='1'
    number = file1.write(number)  
    file1.close()


if __name__=="__main__":
    insert_DB()
    
