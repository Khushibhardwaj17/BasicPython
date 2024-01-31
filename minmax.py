def getMinMax(arr):
    arr.sort()
    minmax={"min":arr[0],"max":arr[-1]}
    return minmax
arr=[1000,4000,300,200,876,259]
minmax = getMinMax(arr)
print("Minimum element is",minmax["min"])
print("Maximum element is",minmax["max"])