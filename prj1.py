n1=int(input("enter marks of test 1:"))
n2=int(input("Enter marks of test 2:"))
n3=int(input("Enter marks of test 3:"))
if n1<=n2 and n1<=n3:
    avgmarks=(n2+n3)/2
elif n2<=n1 and n2<=n3:
    avgmarks=(n1+n3)/2
elif n3<=n1 and n3<=n2:
    avgmarks=(n1+n2)/2
print("Average of best two marks is",avgmarks);