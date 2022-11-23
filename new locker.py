import datetime
TodayDate=datetime.datetime.now()
Name=input("Enter your name")
Password=input("Enter your password")
c="Your user name or password was false try again"
if Name=="Rashid" and Password=="2345":
    print("Welcome")
    print(TodayDate)  
elif Name=="Natasha" and Password=="1234":
    print("Hello""."+Name)
    print(TodayDate)  
elif Name=="Anmol" and Password=="5678":
    print('Hello'"," +Name)
    print(TodayDate)
else:
    print(c)
   


