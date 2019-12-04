import numpy as np

a = np.array([[1,2],[3,4]])
print(a)
if((a != 5).all()):
    print("yes")
else:
    print("no")

b = np.nonzero(a == 2)
print(*b)
print(max(0, 2))
        
