
from ast import Return
from pickle import TRUE
import random
from tkinter import X


print("\n")
print("\t\t**************Welcome To Travelling World****************")
print("\n")
print("\t\t\t\t--------------\t\t\t")
print("\t\t\t\t| Login Page |\t\t\t")
print("\t\t\t\t--------------\t\t\t")
print("\n")

def function():
    First_Name=input("\t\t\t First Name :\t")
    Last_Name=input("\t\t\t Last Name :\t")
    Age=input("\t\t\t Age :\t")
    while True:
        mobile_no=input("\t\t\t Mobile no. :")
        length=len(mobile_no)
        if length == 10:
            return 0
        else:
            print("\t\t\t Invalid mobile number please reenter again....")
        
    print("\t--------------------------------------------------------------")
    print("\n")
    
details={"BUS":{"Mumbai":{  "Arrival":"Pune",
                            "Destination":"Mumbai",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":600,
                            "duration":"4hr"},
                "Thane":{   "Arrival":"Pune",
                            "Destination":"Thane",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":800,
                            "duration":"5hr"},
                "Nagpur":{  "Arrival":"Pune",
                            "Destination":"Nagpur",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":2000,
                            "duration":"13hr"},
                "Nashik":{  "Arrival":"Pune",
                            "Destination":"Nashik",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":1000,
                            "duration":"6hr"},
                "SambhajiNagar":{   "Arrival":"Pune",
                                    "Destination":"SambhajiNagar",
                                    "Date":"27-06-2022",
                                    "Time":"10:30 AM",
                                    "Budgets":1200,
                                    "duration":"6hr"}
                    },
            
        "TRAIN":{"Mumbai":{  "Arrival":"Pune",
                            "Destination":"Mumbai",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":2000,
                            "duration":"2hr"},
                "Thane":{   "Arrival":"Pune",
                            "Destination":"Thane",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":2000,
                            "duration":"2.5hr"},
                "Nagpur":{  "Arrival":"Pune",
                            "Destination":"Nagpur",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":2000,
                            "duration":"12hr"},
                "Nashik":{  "Arrival":"Pune",
                            "Destination":"Nashik",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":2000,
                            "duration":"4hr"},
                "SambhajiNagar":{   "Arrival":"Pune",
                                    "Destination":"SambhajiNagar",
                                    "Date":"27-06-2022",
                                    "Time":"10:30 AM",
                                    "Budgets":2000,
                                    "duration":"4.5hr"}
                    },

        "AIROPLANE":{"Mumbai":{  "Arrival":"Pune",
                            "Destination":"Mumbai",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":3000,
                            "duration":"30min"},
                "Thane":{   "Arrival":"Pune",
                            "Destination":"Thane",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":3500,
                            "duration":"35min"},
                "Nagpur":{  "Arrival":"Pune",
                            "Destination":"Nagpur",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":8000,
                            "duration":"1.20hr"},
                "Nashik":{  "Arrival":"Pune",
                            "Destination":"Nashik",
                            "Date":"27-06-2022",
                            "Time":"10:30 AM",
                            "Budgets":5000,
                            "duration":"45min"},
                "SambhajiNagar":{   "Arrival":"Pune",
                                    "Destination":"SambhajiNagar",
                                    "Date":"27-06-2022",
                                    "Time":"10:30 AM",
                                    "Budgets":5000,
                                    "duration":"45min"}
                    }
            }

admin=input("\t\t\tEnter userId :\t")
password=input("\t\t\tEnter the Password :\t")
if(admin=="abc" and password=="123"):
    print("\t--------------------------------------------------------------")
    #captcha=input("\t\t\tSolve the captcha [25+15]:\t")
    r1=random.randint(1,50)
    r2=random.randint(51,100)
    addition=r1+r2
    print("\t\t\tThe captcha is:\t","(",r1,"+",r2,")")
    
    captcha=int(input("\t\t\tSolve the captcha :\t"))
    #print("\t\t\tCaptcha answer is:\t",r1+r2)
    if(captcha==addition):
        print("\t--------------------------------------------------------------")
        print("\t\t\tYou Are Succefully Logged In.....\t")
        print("\t--------------------------------------------------------------")
        
    else :
        print("\t\t\tInvalid capture...... \t")
        print("\t\t\tRe-enter the capture......")
        captcha=input("\t\t\tSolve the captcha :\t")
else:
    print("\t\t\tinvalid information\t")
    print("\t--------------------------------------------------------------")

print("\t\t\tYour transport mediums are: \n\t\t\t\t\t1)BUS\n\t\t\t\t\t2)TRAIN\n\t\t\t\t\t3)AIROPLANE\n")
transport_medium=input("\t\t\tEnter your transport medium:\t")
print("\t\t\tYour Arrival location is PUNE.")
print("\t\t\tYour Destination's location are:\n\t\t\t\t\t1)Mumbai\n\t\t\t\t\t2)Thane\n\t\t\t\t\t3)Nagpur\n\t\t\t\t\t4)Nashik\n\t\t\t\t\t5)SambhajiNagar")
destination=input("\t\t\tChoose one of them:\t")



if transport_medium=="BUS" or transport_medium=="bus":
    print("\t\t\tDetails as shown below:")
    if destination=="MUMBAI" or destination=="mumbai" or destination=="Mumbai":
        print("\t\t\t\tDate: ",details["BUS"]["Mumbai"]["Date"])
        print("\t\t\t\tTime: ",details["BUS"]["Mumbai"]["Time"])
        print("\t\t\t\tBudgets: ",details["BUS"]["Mumbai"]["Budgets"])
        print("\t\t\t\tduration: ",details["BUS"]["Mumbai"]["duration"])
    elif destination=="THANE" or destination=="thane" or destination=="Thane":
        print("\t\t\t\tDate: ",details["BUS"]["Thane"]["Date"])
        print("\t\t\t\tTime: ",details["BUS"]["Thane"]["Time"])
        print("\t\t\t\tBudgets: ",details["BUS"]["Thane"]["Budgets"])
        print("\t\t\t\tduration: ",details["BUS"]["Thane"]["duration"])
    elif destination=="NAGPUR" or destination=="nagpur" or destination=="Nagpur":
        print("\t\t\t\tDate: ",details["BUS"]["Nagpur"]["Date"])
        print("\t\t\t\tTime: ",details["BUS"]["Nagpur"]["Time"])
        print("\t\t\t\tBudgets: ",details["BUS"]["Nagpur"]["Budgets"])
        print("\t\t\t\tduration: ",details["BUS"]["Nagpur"]["duration"])
    elif destination=="NASHIK" or destination=="nashik" or destination=="Nashik":
        print("\t\t\t\tDate: ",details["BUS"]["Nashik"]["Date"])
        print("\t\t\t\tTime: ",details["BUS"]["Nashik"]["Time"])
        print("\t\t\t\tBudgets: ",details["BUS"]["Nashik"]["Budgets"])
        print("\t\t\t\tduration: ",details["BUS"]["Nashik"]["duration"])
    elif destination=="SAMBHAJINAGARE" or destination=="sambhajinagar" or destination=="Sambhajinagar" or destination=="SambhajiNagar":
        print("\t\t\t\tDate: ",details["BUS"]["SambhajiNagar"]["Date"])
        print("\t\t\t\tTime: ",details["BUS"]["SambhajiNagar"]["Time"])
        print("\t\t\t\tBudgets: ",details["BUS"]["SambhajiNagar"]["Budgets"])
        print("\t\t\t\tduration: ",details["BUS"]["SambhajiNagar"]["duration"])
    else:
        print("Invalid input....")
        destination=input("\t\t\tChoose one of them:")
            
elif transport_medium=="TRAIN" or transport_medium=="train":
    print("\t\t\tDetails as shown below:")
    if destination=="MUMBAI" or destination=="mumbai" or destination=="Mumbai":
        print("\t\t\t\tDate: ",details["TRAIN"]["Mumbai"]["Date"])
        print("\t\t\t\tTime: ",details["TRAIN"]["Mumbai"]["Time"])
        print("\t\t\t\tBudgets: ",details["TRAIN"]["Mumbai"]["Budgets"])
        print("\t\t\t\tduration: ",details["TRAIN"]["Mumbai"]["duration"])
    elif destination=="THANE" or destination=="thane" or destination=="Thane":
        print("\t\t\t\tDate: ",details["TRAIN"]["Thane"]["Date"])
        print("\t\t\t\tTime: ",details["TRAIN"]["Thane"]["Time"])
        print("\t\t\t\tBudgets: ",details["TRAIN"]["Thane"]["Budgets"])
        print("\t\t\t\tduration: ",details["TRAIN"]["Thane"]["duration"])
    elif destination=="NAGPUR" or destination=="nagpur" or destination=="Nagpur":
        print("\t\t\t\tDate: ",details["TRAIN"]["Nagpur"]["Date"])
        print("\t\t\t\tTime: ",details["TRAIN"]["Nagpur"]["Time"])
        print("\t\t\t\tBudgets: ",details["TRAIN"]["Nagpur"]["duration"])
        print("\t\t\t\tduration: ",details["TRAIN"]["Nagpur"]["duration"])
    elif destination=="NASHIK" or destination=="nashik" or destination=="Nashik":
        print("\t\t\t\tDate: ",details["TRAIN"]["Nashik"]["Date"])
        print("\t\t\t\tTime: ",details["TRAIN"]["Nashik"]["Time"])
        print("\t\t\t\tBudgets: ",details["TRAIN"]["Nashik"]["Budgets"])
        print("\t\t\t\tduration: ",details["TRAIN"]["Nashik"]["duration"])
    elif destination=="SAMBHAJINAGARE" or destination=="sambhajinagar" or destination=="Sambhajinagar" or destination=="SambhajiNagar":
        print("\t\t\t\tDate: ",details["TRAIN"]["SambhajiNagar"]["Date"])
        print("\t\t\t\tTime: ",details["TRAIN"]["SambhajiNagar"]["Time"])
        print("\t\t\t\tBudgets: ",details["TRAIN"]["SambhajiNagar"]["Budgets"])
        print("\t\t\t\tduration: ",details["TRAIN"]["SambhajiNagar"]["duration"])
    else:
        print("Invalid input....")
        destination=input("\t\t\tChoose one of them:")
            
elif transport_medium=="AIROPLANE" or transport_medium=="airoplane":
    print("\t\t\tDetails as shown below:")
    if destination=="MUMBAI" or destination=="mumbai" or destination=="Mumbai":
        print("\t\t\t\tDate: ",details["AIROPLANE"]["Mumbai"]["Date"])
        print("\t\t\t\tTime: ",details["AIROPLANE"]["Mumbai"]["Time"])
        print("\t\t\t\tBudgets: ",details["AIROPLANE"]["Mumbai"]["Budgets"])
        print("\t\t\t\tduration: ",details["AIROPLANE"]["Mumbai"]["duration"])
    elif destination=="THANE" or destination=="thane" or destination=="Thane":
        print("\t\t\t\tDate: ",details["AIROPLANE"]["Thane"]["Date"])
        print("\t\t\t\tTime: ",details["AIROPLANE"]["Thane"]["Time"])
        print("\t\t\t\tBudgets: ",details["AIROPLANE"]["Thane"]["Budgets"])
        print("\t\t\t\tduration: ",details["AIROPLANE"]["Thane"]["duration"])
    elif destination=="NAGPUR" or destination=="nagpur" or destination=="Nagpur":
        print("\t\t\t\tDate: ",details["AIROPLANE"]["Nagpur"]["Date"])
        print("\t\t\t\tTime: ",details["AIROPLANE"]["Nagpur"]["Time"])
        print("\t\t\t\tBudgets: ",details["AIROPLANE"]["Nagpur"]["Budgets"])
        print("\t\t\t\tduration: ",details["AIROPLANE"]["Nagpur"]["duration"])
    elif destination=="NASHIK" or destination=="nashik" or destination=="Nashik":
        print("\t\t\t\tDate: ",details["AIROPLANE"]["Nashik"]["Date"])
        print("\t\t\t\tTime: ",details["AIROPLANE"]["Nashik"]["Time"])
        print("\t\t\t\tBudgets: ",details["AIROPLANE"]["Nashik"]["Budgets"])
        print("\t\t\t\tduration: ",details["AIROPLANE"]["Nashik"]["duration"])
    elif destination=="SAMBHAJINAGARE" or destination=="sambhajinagar" or destination=="Sambhajinagar" or destination=="SambhajiNagar":
        print("\t\t\t\tDate: ",details["AIROPLANE"]["SambhajiNagar"]["Date"])
        print("\t\t\t\tTime: ",details["AIROPLANE"]["SambhajiNagar"]["Time"])
        print("\t\t\t\tBudgets: ",details["AIROPLANE"]["SambhajiNagar"]["Budgets"])
        print("\t\t\t\tduration: ",details["AIROPLANE"]["SambhajiNagar"]["duration"])
    else:
        print("Invalid input....")
        destination=input("\t\t\tChoose one of them:")

else:
    Return
            
print("\n\t--------------------------------------------------------------")
n=int(input("\t\t\tEnter no of passengers:"))
print("\t--------------------------------------------------------------")
        
for i in range(1,n+1):
    print("\t\t\tPassenger No:",i)
    function()
    if n == i:
        break
    i+=1

#bill= X * n
if transport_medium=="BUS" or transport_medium=="bus":
    
    if destination=="MUMBAI" or destination=="mumbai" or destination=="Mumbai":
        X=details["BUS"]["Mumbai"]["Budgets"]
        #print(X)
    
    elif destination=="THANE" or destination=="thane" or destination=="Thane":
        X=details["BUS"]["Thane"]["Budgets"]
        
    elif destination=="NAGPUR" or destination=="nagpur" or destination=="Nagpur":
        X=details["BUS"]["Nagpur"]["Budgets"]
    
    elif destination=="NASHIK" or destination=="nashik" or destination=="Nashik":
        X=details["BUS"]["Nashik"]["Budgets"]
        
    elif destination=="SAMBHAJINAGARE" or destination=="sambhajinagar" or destination=="Sambhajinagar" or destination=="SambhajiNagar":
        X=details["BUS"]["SambhajiNagar"]["Budgets"]
        
    else:
        print("Invalid input....")
        destination=input("\t\t\tChoose one of them:")
            
elif transport_medium=="TRAIN" or transport_medium=="train":
    
    if destination=="MUMBAI" or destination=="mumbai" or destination=="Mumbai":
        X=details["TRAIN"]["Mumbai"]["Budgets"]
        
    elif destination=="THANE" or destination=="thane" or destination=="Thane":
        X=details["TRAIN"]["Thane"]["Budgets"]
        
    elif destination=="NAGPUR" or destination=="nagpur" or destination=="Nagpur":
        X=details["TRAIN"]["Nagpur"]["duration"]
        
    elif destination=="NASHIK" or destination=="nashik" or destination=="Nashik":
        X=details["TRAIN"]["Nashik"]["Budgets"]
        
    elif destination=="SAMBHAJINAGARE" or destination=="sambhajinagar" or destination=="Sambhajinagar" or destination=="SambhajiNagar":
        X=details["TRAIN"]["SambhajiNagar"]["Budgets"]
        
    else:
        print("Invalid input....")
        destination=input("\t\t\tChoose one of them:")
            
elif transport_medium=="AIROPLANE" or transport_medium=="airoplane":
    
    if destination=="MUMBAI" or destination=="mumbai" or destination=="Mumbai":
        X=details["AIROPLANE"]["Mumbai"]["Budgets"]
        
    elif destination=="THANE" or destination=="thane" or destination=="Thane":
        X=details["AIROPLANE"]["Thane"]["Budgets"]
        
    elif destination=="NAGPUR" or destination=="nagpur" or destination=="Nagpur":
        X=details["AIROPLANE"]["Nagpur"]["Budgets"]
        
    elif destination=="NASHIK" or destination=="nashik" or destination=="Nashik":
        X=details["AIROPLANE"]["Nashik"]["Budgets"]
        
    elif destination=="SAMBHAJINAGARE" or destination=="sambhajinagar" or destination=="Sambhajinagar" or destination=="SambhajiNagar":
        X=details["AIROPLANE"]["SambhajiNagar"]["Budgets"]
        
    else:
        print("Invalid input....")
        destination=input("\t\t\tChoose one of them:")

else:
    Return

bill= X * n
print("\t\t\tYour total bill amount is :",bill)

print("\n\t\t\tYour details are successfully saved")
print("\n\t\t\tTHANK YOU!")
