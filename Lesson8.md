# Python Collection

## List

> A collection is a group of similar type items stored together

List is one of the 4 different types of collection types in Python

```
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

The above list named "fruits" store string type values in it. 

## Key attributes of a list

> - List items are ordered
- List can store duplicate values 
- The order of the list items can be changed
- List items can be of any data types - String, integer etc, including combination of data types. 
- Items in the list start with an index of 0

```
fruits = [1, "apple", 2, "banana", 3, "cherry"]
print(fruits)

oddNumbers = [1,3,5,7]
print(oddNumbers)

#finding length of the list 
print(len(oddNumbers))

```

## Accessing list items  
> you can access list items by referring to the index number, or a range of index number 

```
fruits = ['apple', 'orange', 'banana', 'strawbery','pineapple','peach']

print(fruits[0])

print(fruits[3:4])

```
> the range allows you to extract a portion of the list. 

> you can also use a negatiev index if you would like to extract the items from the end of the list in reverse


```
fruits = ['apple', 'orange', 'banana', 'strawbery','pineapple','peach']

print(fruits[-1])
print(fruits[-4:-2])
```

> when accessing the list items by a range, you can avoid the starting or ending range value to begin from the start to the end 


```
Names = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']

print(Names[:5])
print(Names[3:])
print(Names[:])
```

> you can use an if condition to check if an items is present in the list

```
Names = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']

if 'Johan' in Names:
  print("Johan is present")

```

### Updating a list 

> You can modify a list with an assignment statement 

```
Names = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']

Names[1] = 'Jayan'

print(Names)

```

> try printing the length of the list before and after the assignment and you will see that the number remains the same. That is because when you use an assignment statement with an index number, it will replace the item and not add/append

> When assigning a value using index, ensure that there is an item at that index or else it will result in error. 

```
Names = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']
Names[6] = input("enter a name : ")
print(Names)

```

> what you just saw is a runtime error and not compile time error. 
- a runtime error occurs when you run the program and not when you compile. 
- a compile time error is usually when you make a syntax error and the program canot compiler error free. In which case you wont be able to run the program.  

You can also change a range of values is a list


```
Names = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']
Names[1:3] = ["Rob", "Sam"]
print(Names)
```


### Inserting item into a list. 

> you can insert an item in the list at specific index or at the end of the list

```
Names = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']
Names.insert(0,'Savita');
print(Names)

Names.append('Lakshmi');
print(Names)
```


### Merging the list 

> you can merge two lists two form one 

```
classAP = ['Matt','Susan','Dan']
classPython = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']
classST = [] #look at this line on why it is needed
classST.extend(classAP)
classST.extend(classPython)
print(classST)

classDuplicate = classAP + classPython
print(classDuplicate)
```

### Remove an item from the list 

> you can remove an item at a specified index or a specific item

```
classAP = ['Matt','Susan','Dan']
classPython = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']
classST = [] #look at this line on why it is needed
classST.extend(classAP)
classST.extend(classPython)
print(classST)

classST.pop(0) # if you do not pass an index it will remove the last item
print(classST)

classST.remove('Dan')
print(classST)
```

> you can also use a del command to remove the items at a specifc index or remove the list itself

```
classAP = ['Matt','Susan','Dan']

del classAP[0]

print(classAP)
 
del classAP

print(classAP) # this should result in error

```

> you can also use the clear function to remove all items from the list

```
classAP = ['Matt','Susan','Dan']
classAP.clear()

print(classAP)
```

### list traversing 

> you can use for loop to iterate through a list 

```
classPython = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']
copyClass =[]

for  student in classPython:
  copyClass.append(student)
  print(copyClass)

```

### sorting items in a list 

```
classPython = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']
classPython.sort()

print(classPython)


primeNumbers = [12,3,5,1,2,4,6,9,8,11,10]
primeNumbers.sort(reverse=true)
print(primeNumbers)
```


# Session work 

> ##  Predict 
what would be the output of the commmands below

```
Names = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']
Names.sort(reverse=False)
print(Names)

```

```
list1 = [1,2,3]
list3 = ['a','b','c']

#list2 = list1 + list3
list1.extend(list3)
list2 = list1#.extend(list3) 
print(list2)
```

> ##  Investigate/Challenge
Find the problem in the code below and fix it

```
Names = ['Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal']
Names.remove[3]
print(Names[3])

```


> ## Develop 
Write a program to accept names of 3 students into a list and create another list to record the grades of the students and merge into a third list 


# Assignment
Accept a long sentence from the user and create a list of each word from the sentence 

