x=[369,367.9,0.9,78,77.77,77.78]
print("Original list",x)
count=0
for i in x:
    count=count+i
avg=count/len(x)
print("Avg is:",avg)
x.sort()    
print("Smallest number in list is",x[0])
print("Largest number in list is",x[-1])
