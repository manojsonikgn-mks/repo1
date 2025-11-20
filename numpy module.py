'''#1-d array
import numpy as np
a=np.array([10,20,30,40])
for i in a:
    print(i,end=",")'''

#2-d array:
'''import numpy as np
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
for i in arr:
    for j in i:
        print(j,end=",")'''

#3-D array:
'''import numpy as np
arr=np.array([[[10,20],[20,30]],[[30,40],[40,50]]])
print(arr)
for i in arr:
    for j in i:
        for k in j:
            print(k,end=",")'''

'''import numpy as np
a=np.array([10,20,30,40,50,60,70,80])
print(a.reshape(2,4))'''

'''import numpy as np
a=np.array([1,2,3,4,5])
print(a.max())'''

#help("numpy")

'''import numpy as np
print(np.info())'''


