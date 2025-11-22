'''data=1215
print(data//2)
print(data//10)'''


#print(2**5)


'''st="Hello Manoj"
print("H" in st)

lst=["manoj","sai","sachin"]
print("manoj" not in lst)'''

'''a=10
print(type(a))

a="hello"
print(type(a))'''

'''st="python manoj"
print(st[0],end=" ")
print(st[6],end=" ")
print(st[8])
print(st[20])#Index Error '''


'''data="python manoj"
print(data[0:])
print(data[:12])
print(data[:])
print(data[0::])
print(data[::-1])
print(data[4:5])
print(data[10:4:-1])
print(data[-4:])
print(data[::]) '''



#print("Ram "*5,end=" ")


'''a="manoj"   
b="kumar"
c="soni"

#print(a,b,c)

print(("_".join([a,b,c])))'''

'''st="manoj"
print(len(st)-1)'''

st="manoj mumar moni"

#b=st.count("x")
#print(b)

#print(st.index("o"))
#print(st.index("i"))

#print(st.find("o"))
#print(st.find("i"))

'''print(st.title())
print(st.capitalize())
print(st.upper())
print(st.lower())
print(st.swapcase())
print(st.islower())
print(st.isupper())
print(st.startswith("m"))
print(st.endswith("moni"))
print(st.replace("m","k"))
print(st.replace("m","-"))'''

#list:

'''a=[1,2,3,"manoj"]
print(a[3])'''


'''lst=[100,20,45,62,35,4,21,"ram"]
print(lst[::])
print(lst[1::])
print(lst[:8:])
print(lst[2:4])
print(lst[::-1])
print(lst[-1:1:-1])
print(lst[1:1])
print(lst[-1:2:-1])'''

'''a=10
b="Python"
c=True
d=10.8

lst=[a,b,c,d]
print(lst)

a,b,c,d=lst
print(a,b,c,d)'''


'''lst1=[10,20,30,"hi"]
lst2=[20,30,15,25,"manoj"]
print(lst1+lst2)'''

lst=[3,5,1,4,0]
#print(lst[1:4]*3)'''
#print(lst.index(4))

'''print(max(lst))
print(min(lst))
print(sum(lst))'''

#print(all(lst))
#print(any(lst))

#print(lst.append(10))
#print(lst)

'''b=lst.extend([3])
b=lst.extend([3,4,45,4,4])
print(lst)'''

'''lst.insert(0,100)
lst.insert(1,-89)
lst.insert(1,90)'''
#print(lst)

'''lst.remove(5)
lst.remove(3)
print(lst)'''
#print(lst)
#lst.pop()
#lst.pop()
'''lst.pop(0)
print(lst)'''

#del lst
'''print(lst)
del lst[1:3]
print(lst)'''

'''a={"name":"manoj","age":23,"address":"motipura"}
#print((a))
print(a["name"])
a["name"]="Sohan"
print(a)
a[True]=1
a["age"]+=20
a["address"]+=" Khargone"


print(a)'''



'''a={"name":"manoj","age":23,"address":"motipura"}
print(a)
a.pop("age")
print(a)'''


a={"name":"manoj","age":23,"address":"motipura"}
'''print(a)
a.popitem()
a.popitem()
a.popitem()
a.popitem()
print(a)'''

#print(len(a))
#print(round(3.6))


student={
"a":{"name":"manoj","age":23,"address":"motipura"},
"b":{"data":123,False:0},
"c":{"marks":514,"fees":[10,20,30]}
}
'''print(student)

print(student["a"]["name"])
print(student["c"]["fees"])
print(sum(student["c"]["fees"]))
print(max(student["c"]["fees"]))
print(student["c"]["fees"][-2])'''


'''lst=[1,2,1,6,8,10,5,3,12]
lst1=[]
lst2=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
    else:
        if i%2!=0:
            lst2.append(i)
print(lst1)
print(lst2)'''

'''st="Python Narayan Tech House"
st1=st.split()
st2=""
for i in st1:
    st2=st2+i[0]    
    
print(st2)'''
    

'''print(a.update(b))
print(a)
print(b)'''

'''print(a.keys())
print(a.values())'''

#print(a.items())

'''def f1(x,y):
    print(x+y)

f1(10,30)'''


'''a=lambda x,y:x+y
print(a(10,20))'''

'''a=lambda x,y:x if x>y else y
print(a(10,20))'''

'''st="hello jaba is very good language"

for i in st.split():
    a=len(i)
    print([a],end="")


print([len(i) for i in st.split()])'''

'''a=open("Hello_file.txt","w")
a.write("Welcome to first file program")
a.close()

b=open("Hello_file.txt","w")
print(b.write("SEcond Data")
b.close()'''


'''a=open("Hello_file.txt","a")
print(a.write(" IT is Append Now"))
a.close()'''

'''a=open("Second file.txt","w")
a.write("Hello it is First line \nHello it is Second line \nHello it is Third line ")
a.close()'''

'''a=open("Second file.txt","a")
a.write("\nLast Line")
a.close()'''

'''a=open("Second file.txt","r")
b=a.read()
print(b)
a.close()
print("---------------------------")

b=open("Second file.txt","r")
s=b.read(4)
print(s)
print("---------------------------")
c=open("Second file.txt","r")
z=c.readline()
print(z)
print("---------------------------")
d=open("Second file.txt","r")
x=d.readline(3)
print(x)
print("---------------------------")'''
m=open("Second file.txt","r")
v=m.readlines()
print(v[0][1:5

           ])
print("---------------------------")










































