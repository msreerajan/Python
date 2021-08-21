# String Operations and Iteration

## String Operations

### What are strings?
> String is a datatype which can store a number of characters together.   

a typical string assignment statement is as below:

```
Guest = "Pratyusha"
print(Guest)
```
The string value can be enclosed in a double quote or single quote.

> multiline values can be assigned to a string like this 

```
longString = """ this is line of the string 
and this is line two 
and this is line three"""

print(longString)
```

### how does python store the String value in memory?
when you declare a string variable, python splits each characters into a separate storage location while maintaining the sequence. 

so what you store a string like this 

Guest = "Pratyusha" 

it stores each letter in the word to a different storage location.


### Calculating string length 
Python has an inbuilt function to check the length of a string. try this - 

```
Guest = "Ron" 
print(len(Guest))
```

### find a string in a string 
It is a common taks in Python that you will have to find the existance of a string in another string. See below example 



```
message = " a lazy fox jumped over the fence!"
i = "fox" in message
print(i)
```

as you see, the result will show True, if the string "fox" is found in the message string or else it will return false. Note that the find function is case sensitive and thus searching for "Fox" is not same as searching for "fox"

### using the operator "not" in the find 

you can consider using the "not" keyword while searching the string to see if a string does not exist in a given string. see the example below 

```
message = " a lazy fox jumped over the fence!"
i = "fox" not in message
print(i)
```

> You can use the output of a find statement anywhere a condition is checked. Below code checks if a string "Smyan" exists in the students string


```
students = "Dia, Pratyusha, Smyan, Ron, Neal"

if "Smayan" in students:
  print("The name Smayan is present in the students string")
```

### Extracting String from a String
Python includes method to extract a range of string from another string. 

```
students = "Dia, Pratyusha, Smyan, Ron, Neal"
oneName = students[5:14]
print(oneName)
```
the first value in the square bracket is the sarting index and the second value is the ending index. You may note that the value is stored from a starting index of 0 

> if you would like to extract the string from the very beginning, then you can leave the starting index blank or if you want to extract from a starting poision to the end of the string, leave the ending index blank

```
students = "Dia, Pratyusha, Smyan, Ron, Neal"
oneName = students[:3]
print(oneName)
oneName = students[5:]
print(oneName)
```

> using a negative index number would return the characters from the end of the string. 


-1 means the last char, -2 is the next to last, and so on. In other words -1 is the same as the index len(s)-1, -2 is the same as len(s)-2.

```
students = "Dia, Pratyusha, Smyan, Ron, Neal"
oneName = students[-4:-1]
print(oneName)
```

### String functions - convert case

> Convert an entire string to upper case

```
message = "the light brown fox jumped over the fence"
print(message.upper())

```

> Convert an entire string to lower case

```
message = "the light brown fox jumped over the fence"
print(message.lower())

```

> you could use the string case conversion functions before performing a string comparison

```
message = "the light brown FOX jumped over the fence"

print("fox" in message)
print("fox" in message.lower())

```
### String functions - Remove whitespace

> you can use the strip() to remove leading and trailing whitespaces from a string 

```
message = " the light brown FOX jumped over the fence "

print(message)
print("fox" in message.strip())

```

### String functions - Split 

> you can use the split([character]) to seprate a string. The split is done where it finds the character in the string. If you do not pass a characted, by default it will consider a space as the split character

```
message = " the light brown FOX, jumped over the fence "

print(message.split(","))

```
### String functions - Replace 

> you can use the Replace(<"string to find", "string to replace") to find and replace a string within a string. 

```
message = " the light brown FOX, jumped over the fence "

print(message.replace("fox","dog"))

```

> if you observe the replace function is unable to find the string "fox" since it is case sensitive. This is where the power of chained functions effective. you can use multiple functions chained together to achieve the result like below 


```
message = " the light brown FOX, jumped over the fence "

print(message.lower().replace("fox","dog"))

```

> while the above mentioned are some of the commonly used string functions, you can find a complete list of string functions [here](https://docs.python.org/3/library/stdtypes.html#string-methods) 

### String formating

> It is common to use string concatination and you will find the concatination using "+" is not allowed with a string and a number

Situations like this you could use the format function as below 

``` 
guest = "Angel" 
age = 10
message = "Hi {}, your age is {}"

print(message.format(guest, age))

```

> you can additionally use an index number if you dont want to mess up the order like this 

``` 
guest = "Angel" 
age = 10
message = "Hi {1}, your age is {0}"

print(message.format(age, guest))

```

### String escape sequence 

> Escape sequences are used in strings to enable incluing string literals in the string. for example you can include a " in your string by escaping it like this 

```
message = "this is a double quotes \""

print(message)

```
you can find a list of all escape sequnces [here](https://docs.python.org/2.0/ref/strings.html)

# Session work 

> ##  Predict 
what would be the output of the commmands below

```
message = " Python is awesome!!!"

result = message.lower().strip().replace("Awesome","Excellent")

print(result)

```

```
message = " Python is awesome!!!"

result = message.upper().strip().replace("AWESOME","Excellent")[-3:-2]

print(result)

```

```
fruits = "apple, orange, banana"

fruit = fruits.split(",")

print(fruit[1])

```


> ##  Investigate/Challenge
Find the reason of the error in the command below

```
fruits = "apple, orange, banana"

fruit = fruits.split(",")

print(fruit[3])

```

Fix the error and observe the output of this code below. Can you figure out the reasoning behind the output
```
message = " Python is awesome!!!"

result = message.Lower().strip().replace("Awesome","Excellent")[2,3]

print(result)
```


> ## Develop 

convert the text belpw 
" this is FUN!!!" 

to 

"THIS IS fun!!!"



# Assignment
1. Accept name from the user and print the length of the name  
