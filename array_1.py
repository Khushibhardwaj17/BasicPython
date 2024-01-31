'''import array as arr
a=arr.array('i',[1, 2, 3])
print("The new created array is:")
for i in range(0,3):
    print(a[i],end="")
print()
b=arr.array('d',[2.5, 3.2, 3.3])
print("\n The new created array ia:")
for i in range(0,3):
    print(b[i],end="")'''
from array import*
vals=array('i',[4,6,1,9,3])
for i in range(0,5):
    print(vals[i],end="")
    print()
vals=vals.reverse()
print(vals)