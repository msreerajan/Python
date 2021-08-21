# Python Iteration continued

## Else condition in while loop

> you can use an optional else in the while loop. Note that this is not a conventional use of else in a while loop in many programming languages. 

The else section in a while loop will execute once when the execution exits the while loop 

```
i = 0

while i<5:
  i+=1
  print(i)
else:
   print(i)
```

Observe that the code will atleast print once whether the while loop condition is met or not

## continue keyword 

> When executing the while loop, if you want to skip the remaining code in the loop and move to the next iteration you can use the keyword continue 

```
i = 0

while i<5:
  i+=1
  if i==2:
    continue
  print(i)
else:
   print(i)
```

Observe the difference in the output from the example earlier. This keyword could be particularly useful when you have a long program in the loop and you have a condition where you do not want the remaining code to run for the current iteration. Such use could make your program run faster. 

## for loop 
> Unlike many programming languages the for loop in Python is a simple way to iterate the elemnts of a collection or string

```
fruits = ['apple', 'orange', 'banana']

for x in fruits:
  print(x)

```
**or**

```
fruit = 'banana'

for x in fruit:
  print(x)
```

### else, continue and pass keywords

the use of else and continue is similar to that of how in the while loop. The pass keyword can be used when you have to use a for loop without statments in it. 

### nested loops 
Like nested if condition you could use a loop inside a loop 


# Session work 

> ##  Predict 
what would be the output of the commmands below

```
fruits = ['banana', 'orange', 'grapes']

for x in fruits:
  if x=='banana':
    continue
  print(x)

```

```
i = 1

while i <= 5:
  for j in range(i):
    print('* ', end="")
  i+=1
  print("")

```

> In the above example note that the print statement uses a second argument, it is to instruct the print that you wish to terminate the line with this character and not the default new line "\n" character. 


> ##  Investigate/Challenge
Find the problem in the code below and fix it

```
fruits = ['banana', 'orange', 'grapes']

for x in fruits:
  if x== banana:
    continue
  print(x)
```

Compare the code and output below 

```
i = 1

while i <= 5:
  for j in range(i):
    print('* ', end="")
  i+=1
  print("")

i = 1
while i <= 5:
  j=1
  while j<=i:
    print('* ', end="")
    j+=1
  i+=1
  print("")

```



> ## Develop 

Gerenate a fibonacci sequence until 25 

> Each number in the sequence is the sum of the two numbers that precede it and the sequence starts with 0, 1  





# Assignment
Accept a number from the user and print a pyramid as shown below with the number of lines the user enters. You will have to use iteration and not the print statement with all the stars in each line. 


> hint - you need two loop inside an outer loop 
 
 if the user enters a value 5, the following output should be printed 
```
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
 ```
