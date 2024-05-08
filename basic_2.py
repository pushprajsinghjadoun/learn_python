# if elif and else condition in python

if 5<2 :
    print(5, "is larger than", 2)
elif 5==2 :
    print(5,"is not equal to",2)
else :
    print(5,"is smaller than",2)        
    
    
    
# use 'pass' when you have an if statement with no content, put in the pass statement to avoid getting an error.    

if 5<2 :
    pass



# while loop in python

i = 1

while i<5 :
    print(i)
    if i==3 :
        break
    i+=1
    
# we can also use 'break' and 'continue'


# 

for x in range(2, 6):
  print(x)
  
  
  
    
# if you do not know how many parameter will be passed then use '*'

def myMultiArg(*arg) :
    print(arg[0])
    
myMultiArg("apple","banana")        


# recursive function

def myrecursivefunction(k) :
    if k==0 :
        return 0
    return k + myrecursivefunction(k-1)

print(myrecursivefunction(5))
    

c = lambda a, b : a*b 
print(c(2,5))    


class Car :
    def __init__(self,name):
        self.name = name
    def __str__(self) :
        return f"{self.name}"    
c1 = Car("Pushpraj")

print(c1)        
print(c1.name)   

class Polo(Car) :
    pass

c2 = Polo("PushpraJ")
print(c2.name)
del c1


# name = input("Enter Username : ")

# print(name)

f = open("README.md","rt")

print(f.read())

print(f.readline())



createFile = open("test.txt", 'x')
createFile.write(f.read())



f.close()


import os 

os.remove("test.txt")