#hollow diamond:
'''n=eval(input("Enter Odd Values only:"))
for i in range(0,n):
    for j in range(0,n):
        if i+j==n//2 or i-j==n//2 or j-i==n//2 or i+j==3*(n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() '''


#butterfly:
'''n=eval(input("Enter Odd Values only:"))
for i in range(0,n):
    for j in range(0,n):
        if j==0 or j==n-1 or (j==(n//2)-1 and 1<=i<=(n-2))or (j==n-2 and 1<=i<=(n-2)):# or i+j==2*(n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#zig zag for row=4:
'''rows=eval(input("Enter rows= "))
for i in range(0,rows):
    for j in range(0,rows+9):
        if (i+j)==3 or i+j==9 or j-i==3 or j-i==9:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#rightangle triangle

'''for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()'''

#inverted right angle:
'''for i in range(5,0,-1):
    for j in  range(i):
        print("*",end=" ")
        j-=1
    print()'''

#left angled trianle
'''n=10
for i in range(n,0,-1):
    for j in range(i):
        print("-",end=" ")
    for k in range(n-j):
        print("*",end=" ")
    for m in range(k):
        print("*",end=" ")
    print()'''

#Inverted Left angled trianle:
'''n=10
for i in range(0,n):
    for j in range(i+1):
        print("-",end=" ")
    
    for k in range(n-i,0,-1):
        print("*",end=" ")

    for m in range(n-i-1):
        print("*",end=" ")
    print()'''

#hollow Square n=5
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#hollow right angle triangle
'''n=5
for i in range(n):
    for j in range(i+1):
        if j==0 or i==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()'''

#up and down diamond:
'''n=5
for i in range(n):
    for j in range(n-i):
        print("-",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for m in range(i):
        print("*",end=" ")
    print()
    
for q in range(1,n):
    for o in range(q+1):
        print("-",end=" ")
    for p in range(n-q):
        print("*",end=" ")
    for z in range(n-q,1,-1):
        print("*",end=" ")

    print()'''

#hollow pyramid:
'''n=5
for i in range(n):
    for j in range(n):
        if i+j==n//2 or j-i==n//2 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#hollow diamond
'''n=5
for i in range(n):
    for j in range(n):
        if i+j==n//2 or j-i==n//2 or i-j==n//2 or i+j==3*(n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#half diamond pattern:

'''n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for k in range(1,n):
    for m in range(n-k,0,-1):
        print("*",end=" ")
    print()'''

#numbered right angle triangle:
'''n=5
for i in range(n):
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()'''

#Floyd`s triangle:
'''n=5
num=1
for i in range(n):
    
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()'''

#0-1 binary trianle n=5:
'''n=5
num=121
for i in range(n):
    for j in range(i+1):
        mod=num%2
        print(mod,end=" ")
        num+=1
    print()'''



#pascals triangle problem:
'''n=7

for i in range(n):
    print("-"*(n-i),end=" ")
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    
    print()'''

#binary pattern triangle:
'''n=5

for i in range(n):
    num=121
    
    for j in range(i+1):
        mod=num%2
        print(mod,end=" ")
        num+=1
    print()'''

#same number in row
'''n=5
num=1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
    num+=1
    print()'''

#print C with stars:
'''n=7
for i in range(n):
    for j in range(n-2):
        if (i==0 and j>0) or (i==n-1 and j>0) or (j==0 and i>0 and i<n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#print X from stars:

'''n=5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#+ sign pattern:

'''n=5
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()'''

# hollow diamond inside square:
'''n=7
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==(n//2)+3:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()'''

#diamond outline with diagonal cross.

'''n=7
for i in range(n):
    for j in range(0,n-1):
        if i+j==n//2 or i-j==n//2 or (j-i==n//2 and j<n-1) or (i+j==3*(n//2) and j<n-1) or (i+j==(n//2)+2 and 1<i<4) or (i==n//2 and j==n-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for k in range(2,n):
        if (i+k==n//2 and k>0) or (i-k==n//2 and k>0) or k-i==n//2 or i+k==3*(n//2) or (k-i==(n//2)-2 and 1<i<4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''



#floyd`s triangle reverse(n=5)
'''n=int(input("Enter row: "))
num=n*(n+1)//2
for i in range(n,0,-1):
    
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()'''

#zig zag (Dynamic):
'''n=25
for i in range(n-(n//2)):
    for j in range(2*n):
        if i+j==n//2 or j-i==n//2 or i+j==((3*n)//2)-1 or j-i==((3*n)//2)-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#hollow pyramid numbered:n=5
def hollowpyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i),end=" ")
        for j in range(1,i+1):
            if j==1 or j==i or i==n:
                print(i,end=" ")
            else:
                print(" ",end=" ")
        print()

hollowpyramid(5)
