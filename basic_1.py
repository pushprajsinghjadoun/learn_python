print("Hello world")

# This is a comment

# declaring variable

a = 1
b = 2 
c = a+b
print(c)


# casting the variable 

d = str(a)
e = float(b)

print(d)
print(type(d))

print(e)
print(type(e))


# assign values to multiple variables in one line:
x, y, z = 'Pushpraj', 'Singh', 'Jadoun'

print(x+' '+y+' '+z)

# unpack a collection

fruits =  ["apple","mango","orange"]

p, q, r = fruits

print(p, q, r)


def addTwoNumber():
    print("Sum is : ",a+b)

addTwoNumber()



import random

print(random.randrange(1, 10))


t = "3"
print(int(t))

print()
for x in "pushpraj":
    print(x)
    

print("us" in "pushpraj")    
print("us" not in "pushpraj")  


s = "Hello world, i am Pushpraj"

print(s[0:5])
print(s[-5:])
print(s.strip())


print(f"two number are {a} {b}")



def functionThatReturnTrue() :
    return True

print(functionThatReturnTrue())


if functionThatReturnTrue() :
    print("Yes, true value returned")



# List 

myList = ["apple","mango","organge"]
print(myList[0])    

# List using list() constructor

secondList = list(("apple","mango","organge"))

# insert method insert the element in a specified index
secondList.insert(0,"guava")
secondList.append("banana")

print(secondList)

# to append another list to current list using extend() method
myList.extend(secondList)
print(myList)

myList.remove("organge")
myList.pop(1)

myList.sort(reverse=True)
myList.reverse()

del secondList

myList.clear()
print(myList)



# Tuple

thisTuple = ("apple","mango","organge","tuple")
secondTuple = tuple(("apple","mango","organge"))
print(thisTuple)
print(secondTuple)

# Once tuple is created we can not change the tuple value, to do so we have to convert it into list and change the value and again convert it into tuple

listTuple = list(thisTuple)
listTuple[3] = "new tuple from list"
thisTuple = tuple(listTuple)

print(thisTuple)


# set 


mySet = {"apple","mango","banana"}
secondSet = set(("apple","mango","banana"))
print(mySet)

for x in mySet:
    print(x)
    
    
secondSet.add("guava")
print(secondSet)   

mySet.update(secondSet)

print(mySet) 

# remove method will raise error if "apple" does not exist, to prevent this error use discard() method
mySet.remove("apple")

mySet.discard("pushpraj")

print(mySet)

set3 = mySet.union(secondSet)
print(set3)



# Dictionaries 

myDict = {"name":"Pushpraj", "age":23}
print(myDict)
print(myDict["name"])
secondDict = dict(name="Pushpraj", age = 23)
print(secondDict)
print(len(myDict))

print(myDict.keys())
print(myDict.values())
print(myDict.items())

if "Pushpraj" in myDict.values() :
    print("Yes, exist")
    
    
myDict.update({"name":"Pushpraj Singh Jadoun"})
myDict["place"] = "Indore"
print(myDict)    