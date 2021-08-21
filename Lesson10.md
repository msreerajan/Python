# Dictionary 

> Python provides a collection of key value pairs which allows to store and retrieve an item by key. 

Syntax  
DictionaryName = {

  <KeyName>:<Value>,  
  <KeyName>:<Value>  
  ...  
}


Consider the below example:

```
students = {
  1:"Johan",
  2:"Ron",
  3:"Smyan",
  4:"Neal"
}

print(students) # print entire Dictionary
print(students.keys()) # print all the keys in the Dictionary
print(students.values()) # pring all the values in the Dictionary
print(students[4]) # print a specific item against a key
```

> Since the key is used to identify an item in the Dictionary, it can also be referred as an identifier

### accessing an item

> you can refer to the key to retrieve an item from the Dictionary

The example below will retrieve the item with key 2
```
a = students[2] 
```
### assigning a value 
you can update/assign a value to a key using the assingment statement 

```
students = {
  1:"Johan",
  2:"Ron",
  3:"Smyan",
  4:"Neal"
}
students[1] = "Pratyusha"
print(students)
```

### check if a key exists 
> You can check if a key exists in the Dictionary

```
students = {
  1:"Johan",
  2:"Ron",
  3:"Smyan",
  4:"Neal"
}

if 4 in students:
  print(students[4])

```
## adding an item to the Dictionary

> You can add an item to the Dictionary by using a new key and assign a value to it. 

```
students = {
  1:"Johan",
  2:"Ron",
  3:"Smyan",
  4:"Neal"
}
students[5] = "Pratyusha"
students[6] = "Dia"

print(students)
```
## removing an item

> you can remove an item from Dictionary using the pop method

```
students = {
  1:"Johan",
  2:"Ron",
  3:"Smyan",
  4:"Neal"
}
students[5] = "Pratyusha"
students[6] = "Dia"

students.pop(2)
students.popitem() 

print(students)
```
> note that the popitem method will remove the last inserted item from Dictionary

### Nested Dictionaries

> is useful when you have repeated collection of information to be stored against a key. For example storing information of students in a class. 

>> a student will have the following attributes:
First Name, Last Name, Age, Class, School etc. In order for us to store all this information together, we may have to create an individual list for each of those attributes.

> Let us see how can we create this in a dictionary
 
```
students = {
  1: {"Name":"Pratyusha",
      "Grade":10, 
      "School":"NHS"},
  2: {"Name":"Dia",
      "Grade":10, 
      "School":"NHS"}
}
students[3] = {}
students[3]["Name"] = "Neal"
students[3]["Grade"] = 9
students[3]["School"] = "TBD"
print(students)
```

# Python exercises 

## 1. Print all integers from -50 to 50 
## 2. Create a list to accept 10 students grade and find the top 5, bottom 5, average class grade
## 3. Accept a string from the user and remove all special characters from it - ~!@#$%^&*()_+

## Assignment 
Develop a cypher/decypher program which will convert english into jibberish/obfuscated language and transfer it to another person. The other person then could use the same tool to decypher it. 

> for example 

>> I may generate a text = "This is a secret" and the program could produce "kln kj i lkjljt" whic then I may send it to someone i want to share the program. As long as they have the program they can convert it back. 
  
>> Hint to develop - for alphabets a-z find replacing characters. it could be the reverse of the alphabets like - instead of character 'a' you could use 'z', instead of 'b' you could use 'y', so on and so forth. 

>> or you could use numers for each alphabets - like 10 for 'a', 20 for 'b' etc. 

>> Once you have the mappings, you can write a program to conver the letters you enter into the prompt

