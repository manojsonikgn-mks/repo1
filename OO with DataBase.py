class marksheet:
    iname="Ranjan"
    salary=3500000

    def __init__(self,s_name,s_marks):
        self.s_name=s_name
        self.s_marks=s_marks

    def grade(self):
        print("Teacher Name is= ",self.iname," and salary= ",self.salary)
        
        if self.s_marks>=0 and self.s_marks<=30:
            print(self.s_name," Failed")
        elif self.s_marks>30 and self.s_marks<=100:
            print(self.s_name," Passed")
        else:
            print("Invalid Entry")


obj1=marksheet("Manoj",96)
obj1.grade()
obj2=marksheet("Shyam",29)
obj2.grade()

import pymysql
c=pymysql.connect(host="localhost",user="root",password="Abcd@1234",db="studentdb").cursor()
c.execute("select * from studentdata;")
data=c.fetchall()
print(data)
