# Basic command syntax, comments, input, variables

## Basic command syntax

### Indentation
> It is important to structure your code so to make it readable and easy to investigate in the event of troubleshooting. While better readability is the main reason for indenting the code in most languages, in Python indentation acts like block/unit of code. 

Example

```
A condition 
  some code 
  some more code 
  even more code 

```

In the code above, 3 lines starting after "a condition" is considered as a block of code. In other languages the block is defined by marking it with a paranthesis "{ }". All code lines in the same block should use the same indendtation

**NOT indenting a block will result in a syntax error**

> a space or  tab can be used for indentation

### Comments
It is a good practice to comment your code. This will greatly help when you are working in a team and someone other than the author will have to investigate/update/troubleshoot the code 

> a single line of comment is marked by using the symbol "#"

 
>try the below code to see if this will result in an error

```
# PrInT("this text should not result in error")

```

> a multiline comment can be done by added by enclosing the comment text within in a pair of """ """ 

> let us try 

```
"""
This is a comment 
this is another comment 
this is a third line of the comment. 
"""
```
### User Input

It is essential for programs to provide an interface for users to interact with the program. This allows the program to get the code behave based on the specific entries by the user. 

> let us try - to print anything on the screen. 
use the following command

```
input()

```

when you execute the above statement, the prompt remains until you enter text and press the "Enter" key 

however the value you entered cannot be used for processing as it is not stored anywhere so you can refer to it. 

what we need is to be able to temporarily refer to the stored value by a name

>for example let us accept the name of the user and display a welcome message 

```
guest = input()

print("Welcome " + guest)

```

upon executing the above statement, you can see the prompt is waiting for the user to enter a value. Once the user enters the value and press the "Enter" key, a welcome message is then displayed. 

Now you must be wondering, wouldn't it be nice if we could show a message while prompting for the input so the user know the system is ready to accept input. 

> input like print is a function and it internally has an option to show a message while accepting an input. 

> let us try this 

```
guest = input("Please enter your name : ")

print("\n Welcome!" + guest)

```

### Variable 
- In the above example when you used a name for referring the input value form the user, you are actually using a variable.  
- unlike other programming languages Python does not require a declarative statement to define a variable 

Here are some rules for defining a variable 
- you can use any name for a variable 
- you cannot use spaces in the name 
- within the scope you cannot use same name for two variables
- names are case sensitive, you will have to use the same way you have declared the variable 
- name cannot start with a number 
- can only include alpha-numeric characters, underscore and hyphen



### Casting 
when you get a user input into a variable. It is stored as a string and thus you cannot perform any arithemtic operation with the variable. Inorder for you to do that, first you will have to convert the value to an integer.

> there are specific functions to be called to covert the value 

- str(value) - passed value is converted to string 
- int(value) - passed value is converted to integer 
- float(value) - passed value is converted to float/decimal

>try this example 

```
number = input("Enter a number")
print(number + 1)

```
Observe the error and now try this alternate code 
```
number = int(input("Enter a number"))
print(number + 1)
```

# Session work 

> ##  Predict 
what would be the output of the commmands below

```
# print("Learning python is awesome")

```

```
i = 10

print (i + 1)

```

```
i = 11
print(i/2)
```

```
SchoolName = input("Enter the name of your school :")

print(SchoolName + " is awesome);

```

> ##  Investigate/Challenge
Find the reason of the error in the command below

```
Guest = input("Please enter your name : ")

print("\n Welcome!" + guest)

```

Fix the error and observe the output of this code below. Can you figure out the reasoning behind the output
```
j = intput("Enter a even number : ")
result = j%2;
print(result)
```


Fix the code below to run
```
pi = 3.14 
r = 2
print("The area of a circle with radius 2 is :" + pi * r * r)
```

> ## Develop 

accept name, address of the user and print a mail label 



# Assignment
1. Explain what are variables and why is casting needed?
2. what is the difference between the operators "/" and "%" in an arithemtic operation
2. Write a program to accept values for "a" and "b" from the user in the algebraic expression and find the solution 
a^2 + 2ab + b^2
