import  numpy as np
import  time

print("Program Output")

a = np.array([ 1, 2 , 3 , 4])
#print(a.shape)
b = np.random.rand(3)
c = np.random.rand(3)

tic = time.time()
d = np.dot(b,c)
toc = time.time()
Vec_time = toc - tic 
print(b)
print(c)
print(b.shape)
print(c.shape)
print(d)

x = [[1, 0], [0, 1]]
print(len(x))


