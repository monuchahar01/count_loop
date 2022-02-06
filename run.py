#import smtplib, ssl
#import bs4,webbrowser
#import requests
#import time


def count_loop():


    print('Runnning in a count-loop function\n')
    file1 = open("data.txt","r")  
    number = file1.read() 
    file1.close() 
    print('your running number is {}'.format(int(number)))
    file1 = open("data.txt","w")
    number=str(int(number)+1)
    if number == '11':
        number='1'
    number = file1.write(number)  
    file1.close()
    

 


if __name__=="__main__":
    count_loop()
    
    
