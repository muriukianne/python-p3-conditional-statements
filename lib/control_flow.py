#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin" and password == "12345":
        return ("Access granted")
    elif username == "ADMIN" and password == "12345":
        return("Access granted")
    else:
        return("Access denied")    
admin_login("admin","12345")    
    
    

def hows_the_weather(temperature):
    if temperature == 33:
        return("It's brisk out there!")
    elif temperature == 55:
        return("It's a little chilly out there!")    
    elif temperature == 99:
        return("It's too dang hot out there!")   
    elif temperature == 75:
        return("It's perfect out there!")     

hows_the_weather(33)

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return ("FizzBuzz")
    elif num % 3 ==0 and num % 5 != 0:
        return  ("Fizz")
    elif num % 3 != 0 and num % 5 ==0:
        return("Buzz") 
    else:
        return(num)   

def calculator(operation, num1, num2):
    if operation == "+":
        return (num1+num2)
    elif operation == "-":
        return (num1-num2)    
    elif operation == "*":
        return (num1*num2)   
    elif operation == "/":
        if num2 == 0 :
            return("None")
        return (num1/num2)    
    else:
        print("Invalid operation!")     
   
 
