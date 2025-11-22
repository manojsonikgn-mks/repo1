class employee:
    iname="Manoj"
    loc="Hyd"
    salary="3000000"
    company="TCS"

    def __init__(self):
        print("I am a constructor")

    def working(self):
        print("I am working with TCS now")

    def rest(self):
        print("I am resting after work")
        
#option 01:
employee()
employee.rest(5)
print(employee.loc)

#option 02:
'''print(obj.iname)
print(obj.loc)
print(obj.salary)
print(obj.company)

obj.working()
obj.rest()'''
