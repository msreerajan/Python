# Error Handling 

> It is critical that you handle errors/exceptions in your programming to ensure the program does not terminate when error occurs 
>>Here are some of the best practices of error/exception Handling
- code should be able to recover from an unexpected outcome without terminating the program 
- code should communicate with the user in meaningful ways notifying that an error has happened
- when possible always provide detailed error messages to the user with guidance on how to overcome the problem 
- record the error, so you can take a look at the error at a later time. This can be done by saving the details of the error permanently onto a file or other storage options or even send an email  

```
#this should result in an error 
print(name)
```

> let us see how to gracefully handle this error so that, the user wont be seeing system error 

```
try:
  print(studentName)
except:
  print("an error occured")
```
> you can find a full list of built-in exceptions [here](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)


## the finally block 

> the finally block can be included in the exception handling and will be executed regardless of an exception/error occured or not 

```
try:
  print(studentName)
except NameError:
  print("an error occured")
finally:
  print("this will be printed regardless")
```


## raise application exception

> you can chose to raise an exception to skip code blocks based on certain conditions. 

```
try:
  age = int(input("Enter your age:"))

  if age <18:
    raise Exception("You are not old enough to vote!")
except NameError:
  print("an error occured")
except:
  print("Error")
finally:
  print("this will be printed regardless")
```


# File Handling 

> Python includes built-in funtions to handle file operations - read/write 

>> To open a file to read 

```
file = open("Notes.txt")
print(file.read())
```

# Develop

> Write a program to accept the age and suggest if the user is eligible for voting 
>> include exception handling to show error message if the user enters alphabets instead of numbers 

> Download a text file from internet and add it to the library and read it. 
