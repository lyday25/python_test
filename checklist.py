# python code to add cassava to a list of item given
listofitems=["cucumber" , "kola" , "groundnut" , "pineapple" , "carrot" , "grape"]
listofitems.append("cassava")
print(listofitems)

#check if carrot is in the list
for i in listofitems:
    if i=="carrot":
        print("Yes carrot is there")

#python code that loops through the list and print them out
for y in listofitems:
    print(y)
    
#python code that removes kola from the list
listofitems.remove("kola")
print(listofitems)