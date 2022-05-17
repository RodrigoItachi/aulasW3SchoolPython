x = 5       # is of type int
y = "Jhon"  # is of type str

print("-"*45)

print(x)
print(y)


print("-"*45)

a = str(3)      # a will be '3'
b = int(3)      # b will be 3
c = float(3)    # c will be 3.0

print("a will be",a,"\nb will be",b,"\nc will be",c)

print("-"*45)

#   Variable Names

myvar = "John"
my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(myVar)
print(MYVAR)
print(myvar2)

print("-"*45)
#   Multi Words Variable Names

myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

print(myVariableName)
print(MyVariableName)
print(my_variable_name)

print("-"*45)


#   Global Variables

nome = "awesome"

#   Exemplo 01:
# def myFunc():
#     print("Python is "+nome)
    
# myFunc()


#   Exemplo 02:
def myFunc():
    nome = "fantastic"
    print("Python is "+nome)
    
myFunc()

print("Python is "+nome)