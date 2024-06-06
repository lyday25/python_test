# Write a python code that will add list of numbers together
list1=[12,154,79,134,3,10]
sum=0

for i in list1:
    sum=sum+i
print(sum)

if sum>50:
    print("Is the total greater than 50?")
    result=(sum/20)+19
    print(result)
else:
    output=sum+500
    print(output)