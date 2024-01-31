def reveselist(A,start,end):
    while start<end:
        A[start],A[end]=A[end],A[start]
        start += 1
        end-= 1
A=[1,2,3,5,8,9]
print(A)
reveselist(A,0,5)
print("Reverse list:")
print(A)