#01:odd or even number:

'''if num%2==0:
    print("Even")
else:
    print("ODD")'''
#________________________________

#02:largest of three:
'''num1=eval(input("Enter Three Numbers: "))
num2=eval(input("Enter Three Numbers: "))
num3=eval(input("Enter Three Numbers: "))
if num1>num2 and num1>num3:
    print("num1 is greater: ")
elif num2>num1 and num2>num3:
    print("Num2 is Greater: ")
else:
    print("Num3 is graeter: ")'''
#________________________________

#03:percentage:
'''per=eval(input("Enter Percentage achieved by Student: "))
if per>=0 and per<=60:
    print("Grade F")
elif per>60 and per<=70:
    print("Grade D")
elif per>70 and per<=80:
    print("Grade C")
elif per>80 and per<=90:
    print("Grade B")
elif per>90 and per<=100:
    print("Grade A")
else:
    print("Enter Valid Percentage")'''
#________________________________

#04:vowel or consonant:
'''letter=input("Enter Letter: ")
if letter=="a" or letter=="i" or letter=="o" or letter=="e" or letter=="u":
    print("{} is a vowel".format(letter))
else:
    print(f"{letter} is a consonant")'''
#________________________________

#05:Leap Year:
'''year=eval(input("Enter Year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("Leap Year")
else:
    print("Not Leap Year")'''
#________________________________

#06:Basic Calculater:
'''num1=eval(input("Enter First Number"))
num2=eval(input("Enter second Number"))

#operator=   operators=+(add)
 #           -(Subtract)
  #          *(Multipication)
   #         /(Division)
print(operator)
print("select from the operator:")
opt=input("Enter operator")
if opt=="+":
    print(f"{num1}+{num2}= ",num1+num2)
elif opt=="-":
    print(f"{num1}-{num2}= ",num1-num2)
elif opt=="*":
    print(f"{num1}*{num2}= ",num1*num2)
elif opt=="/":
    print(f"{num1}/{num2}= ",num1/num2)
else:
    print("Invallid Syntax") '''
#_______________________________________


#07:positive or negative
'''num=eval(input("Enter Number: "))
if num<0:
    print(f"{num} is negative")
elif num==0:
    print(f"{num} is Zero")
else:
    print(f"{num} is Positive")'''
#______________________________________

#08: loginpage:

'''username=input("Enter Username: ")
password=eval(input("Enter PAssword: "))
if username=="Admin" and password==1234:
    print("Login Successful!!!")
else:
    print("Login Failed!!! Try Again!!!")'''
#_____________________________________

#09:check triangle or not:
'''edge1=input("Enter Edge1: ")
edge2=input("Enter Edge2: ")
edge3=input("Enter Edge3: ")
if edge1+edge2>edge3 or edge2+edge3>edge1 or edge3+edge1>edge2:
    print("Proper Triangle")
else:
    print("Invalid Edges")'''

#_______________________________

#10: BMI(Body Mass Index):
'''height=eval(input("Enter Height(meters): "))
weight=eval(input("Enter Weight(KG): "))
BMI=weight/(height**2)
if BMI>0 and BMI<18.5:
    print(f"{BMI} is Underweight")
elif BMI>=18.5 and BMI<24.9:
    print(f"{BMI} is Normal")
elif BMI>=24.9 and BMI<29.9:
    print(f"{BMI} is overweight")
else:
    print(f"{BMI} is Obesity")'''
#___________________________________

#11:Discount by Price:
'''price=eval(input("Enter Price: "))
discount=0
if price>1000:
    discount=(price*10)/100
    print("Discount= ",discount)
    price=price-discount
    print("After 10% DIscount Price= ",price)
elif price<=1000 and price>500:
    discount=(price*5)/100
    print("Discount= ",discount)
    price=price-discount
    print("After 5% Discount price= ",price)
else:
    print("No Discount")'''
#_____________________________________-

#12: Month-Days:
'''print("Please use small letters only to write!!!")
monthname=input("Enter Name of Month: ")
if monthname=="january" or monthname=="march" or monthname=="may" or monthname=="july" or monthname=="august" or monthname=="october" or monthname=="december":
    print(f"No.of Days in {monthname} is: ",31)
elif monthname=="february" or monthname=="april" or monthname=="june" or monthname=="september" or monthname=="november":
    print(f"No.of Days in {monthname} is: ",30)
else:
    print("Enter Correct month")'''

#_______________________________________

#13: ATM:
option='''Options:
          1:deposite money
          2:withdraw money
          3:check balance '''
print(option)
opt=eval(input("Enter option What you wnat to do: "))
#depamt
withamt=0
#balance
if opt==1:
    global depamt=0
    global balance=0
    depamt=eval(input("Enter amount to be deposite: "))
    print("Previous balance= ",balance)
    balance=balance+depamt
    print(f"After deposite of {depamt} current balance= ",balance)


    


    
