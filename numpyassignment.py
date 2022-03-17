import numpy as np
#1. Create a null vector of size 10 but the fifth value which is 1.

x=np.zeros(10,dtype=int)
x[4]=1
print(x)
#2. Create a vector with values ranging from 10 to 49.

vector=np.arange(start=10,stop=50,step=1,dtype=int)
print(vector)

#3. Create a 3x3 matrix with values ranging from 0 to 8
matrix=np.random.randint(low=0,high=8,size=(3,3),dtype=int)
print(matrix)
#4. Find indices of non-zero elements from [1,2,0,0,4,0]
x=[1,2,0,0,4,0]
for i in range(len(x)):
    if x[i]!=0:
        print(i)
#5. Create a 10x10 array with random values and find the minimum and maximum values.
m1=np.random.randint(low=0,high=101,size=(10,10),dtype=int)
print("minimum element:",m1.min())
print("maximum element",m1.max())
#6. Create a random vector of size 30 and find the mean value.
s=np.random.randint(low=0,high=30,size=(30))
print("mean of vector size 30:",s.mean())
