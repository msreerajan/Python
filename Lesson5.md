# Python Operators and Iteration

## Operators

> Python offers a wide range of operators:
- Arithmetic operators +, -, *, /, %, **
- Assignment operators =, +=, -=, /= 
- Comparison operators ==, !=, >, <, >=, <=, 
- Logical operators and, or, not
- Bitwise operators & (and), |(or), ^(XOR), ~(NOT)
- Identity operators is, is not 
- membership operators in, not in 

> the differnce between "=" and "==" is that one equal is an assignment operator while two equal sign is used to check equality 


### nested if and multiple conditions using logical operators

``` 
i = int(input("enter zero"))

if i==0:
  print("value of i is zero")
else:
  print("you did not enter zero")

``` 


> See below example for a nested if

```
number = int(input("enter an even number greater than 10:"))

if number/2==0:
  if number >10:
    print(str(number) + " is even and greater than 10")
  else:
    print(str(number) + " is even but not greater than 10")
else:
  print(str(number) + " is not even")

```

> the above example uses nested if conditions and it can also be done with single if construct with multiple conditions and logical operators like below 

```
number = int(input("enter an even number greater than 10:"))

if number%2==0 and number>10:
  print(str(number) + " is even and greater than 10")
elif number%2==0 and number<10:
  print(str(number) + " is even but not greater than 10")
elif number%2!=0 and number >10:
  print(str(number) + " is not even but greater than 10")
elif number%2!=0 and number <10:
  print(str(number) + " is not even and not greater than 10")
else:
  print(str(number) + " is even and 10")

```

## Iteration

Iteration is used for repeating a set of statements and the iteration is usally repeated until a condition is met.

> Example - 

Set the condition to true 

while **condition is true**  
  Execute this line  
  at some point **set the condition to False**

> See the code below 

```
number = 0 
while number < 10:
  print( str(number) + "\n")
  number= number +1 

```
> why is that last line important - number = number + 1 ??

### using the break statement to exit 

> you can also use the "break" statement to exit an iteration

```
number = 0 
while number < 10:
  print( str(number) + "\n")
  number= number +1 
  if number>5:
    break
```

# Session work 

> ##  Predict 
what would be the output of the commmands below

```
i = 20

if i !=20 or i>10:
  print("the value of is never less than 10")

```

```
i = 10

while i <10:
  print(i)
  i = i+1

print("iteration is done")

```

```
i = 0
while i <20
  if i%2==0:
    print(str(i) + " is even")
  else:
    print(str(i) + " is odd")

```


> ##  Investigate/Challenge
Find the problem in the code below and fix it

```
i = 0
while i <20
  if i%2==0:
    print(str(i) + " is even")
  else:
    print(str(i) + " is odd")

```

Fix the error and observe the output of this code below. Can you figure out the reasoning behind the output
```
studentNames = "Pratyusha, Ron, Johan, Dia, Neal, Smyan"

if 'Ron' in studentNames OR 'Johan' in studentNames:
  print("Ron is present in the names")
else
  print("Johan is present in the names")

```



> ## Develop 

Accept a number from the user and print all even numbers from 0 to the entered number 



# Assignment
1. Accept a number from the user and find all prime numbers between 0 and that number 
