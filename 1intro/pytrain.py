
# data type
type(10)
type(3.14)
type("hello")

# variable
x = 10
print(x)
x = 100 
print(x)
y = 3.14
print(x*y)
type(x*y)

# list
a = [1,2,3,4,5]
print(a)
len(a)
print(a[0])
print(a[4])
a[4] = 99
print(a)
print(a[0:2]) #index 0->1 not index2
print(a[1:])  #index 1->last
print(a[:3])  #index 0->2 not index3
print(a[:-1]) #Get from the beginning to the one before the last element
print(a[:-2]) #Get from the beginning to the two before the last element

# dictionary
me = {"height":158}
print(me)
me["height"]
me["weight"] = 43
print(me)

# bool
hungry = True
sleepy = False
type(hungry)
print(not hungry)
print(hungry and sleepy)
print(hungry or sleepy)

# if 
hungry = False
if hungry:
	print("I'm hungry")
else:
	print("I'm not hungry")
	print("I'm sleepy now")

# for
for i in [1,2,3]:
	print(i)

# function
def Hello():
	print("HELLO WORLD")

Hello()

def Hello_plus(obj):
	print("HELLO "+obj+" !")

Hello_plus("CAT")


