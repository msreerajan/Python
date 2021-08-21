# Python Functions 

> All programming languages consists of built-in functions. When you use a print function, you are using an abstracted ready to use code and all you know is just call the name of the function. for example 

```
print("hello world!")
```

> The command above will print "hello world" on to the screen and you do not have to know the complexity of the print function, and how it gets it printed on the screen. The same way you use a fully cooked packged meal, where you do not have to know about the ingredients and the process of how it is made. 

> Functions are reusable blocks of code accomplishing a specific purpose. Programming languages included several commonly used code as built-in functions. A collection of built-in functions are wrapped in a package called library or module. 

- a function accomplish one specific purpose
- a function name is always unique in the module/library 
- a function can accept input values to be processed and are called parameters, arguments - e.g. print(**"Hello World"**)
- a function sometimes can return a value - e.g. a = input("enter a number")

> Let us see the structure of a function 

>> def <functionname>([optional list of parameters]):  
      body of the function 

```
# this is a simple function to print hello
def printHello():
  print("Hello") 
```
### calling a function 

> Calling a funtion is simple, just mention the name of the funciton with ()

```
printHello()
```

> The above function call can be repeated any number of time to print "hello"

### function input values/parameters

> You can send input values to the function which are also called input parameters or agrugments. This allows a programmer to interact with the function for some dynamic behavior. 

>> Let us modify the above code to input a name and print the name with the "Hello" message 

```
# function definition
def printHello(name):
  print("Hello, " + name " !")

```

>> The above code allows us to pass any name to the function and print a hello message. The ability to pass different values and print different names is the dynamic behavior mentioned earlier. 

```
#function calling
printHello("Ron")
printHello("Johan")
printHello("Smyan")
```

>> You can set a default value to a parameter, so that when a programmer does not pass the value the default value defined in the function will be used. 

```
# parameter with default value
def printHello(name="Pratyusha"):
  print("Hello, " + name " !")

#when the value is not passed, the function uses the default value
printHello()
```

>> a few important facts about the function parameters 
- You can send any type as parameters 
- each function call should pass the expected number of parameters as defined in the function 
- each parameter should be passed in the same order as it is defined, unless you use paramter names when passing in value 
- if you set a defult vlaue for a parameter in the function definition, passing parameter is then optional. However, if there are multiple parameters passed, all parameters with default values should be at the end. And all parameters without default vaue should be inthe beginning of the list.  

```
# All default value parameter should be at the end of the parameter list
def hello(school , name = "Pratyusha" ):
  print("Hello " + name )
  print(school)


hello("NHS")
```

```
#if you use parameter names while calling the function, you can pass the parameters in any order
def hello(school , name = "Pratyusha" ):
  print("Hello " + name )
  print(school)

hello(name = "Dia", school = "NHS")
```

### a function can return a value

> You can write a function which can return a value 

``` 
# function to return the area of a rectangle 
def areaTriangle(length, width):
  return length*width


area = areaTriangle(10, 20)
print(area)

print(areaTriangle(2,4))
```

# Session work 

> ##  Predict 
what would be the output of the commmands below

```
def try():
  print("a function call")

```

```
def mathOperation(number1=0, number2=0):
  return number1 * number2


print(mathOperation())
```

> ##  Investigate/Challenge
Find the problem in the code below and fix it

```
def mathOperation(number1, number2):
  return number1 + number2


print(mathOperation())

```

```
def mathOperation(number1=10, numner2):
  return number1 + number2


print(mathOperation(10))

```


> ## Develop 
Rewrite the calculator program using functions


# Assignment
Rewrite the cypher/decypher program using functions
