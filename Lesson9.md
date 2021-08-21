# Python Collection - Continued 

## Tuple

> Simliar to List, **tuple** is another type where you can store a collection of items. The key difference is that you cannot add, remove or change items in a tuple after it is created. In other way you can say that tuples are immutable (cannot be changed)

```
tupleStudents = ('Johan','Neal','Ron')

print(tupleStudents)
```



> The below lines if code are not vaid and will result in error. 

```
tupleStudents = ('Johan','Neal','Ron')

tupleStudents[1] = 'Smyan'
print(tupleStudents)
```

## Set

> Simliar to List, **Set** is another type where you can store a collection of items. The key difference is that you cannot remove or change items in a set after it is created. In addition to this Set is unordered, unindexed and cannot store duplicate values.  You can always add new item to the set after it is created. 

```
setStudents = {'Johan','Neal','Ron'}

print(setStudents)
```



> The below lines if code are not vaid and will result in error. 

```
setStudents = {'Johan','Neal','Ron'}

setStudents[1] = 'Smyan' #assingmment statement is not supported
print(setStudents[1]) # reference using index is not supported
```

### Add set items
> you can add new item to a set using the Add method 

```
setStudents = {'Johan','Neal','Ron'}
print(setStudents)
setStudents.add('Pratyusha')
print(setStudents)
setStudents.add('Smyan')
print(setStudents)

```

> as you see the items each time printed is in different order. 

### Remove set items 

> you can remove an item from a set using the remove/discard methods


```
setStudents = {'Johan','Neal','Ron'}
print(setStudents)
setStudents.add('Sam')
print(setStudents)

setStudents.remove('Sam')
print(setStudents)
```

> the key difference between the remove and discard method of set is that, the remove method will return an error if the item is not found, while the discard method does not

```
setStudents = {'Johan','Neal','Ron'}
setStudents.add('Sam')
setStudents.remove('Dia')
print(setStudents)

```

```
setStudents = {'Johan','Neal','Ron'}
setStudents.add('Sam')
setStudents.discard('Dia')
print(setStudents)
```

> you can optionally use the pop method to remove the last item from a set. Since set is not indexed you cannot pass an index number to it 


### clear and delete 

> you can use clear method to empty a set, while del keyword to delete the list itself. 


## Set operations 

> Set operations allow you to operate two sets. Following are some of the set operation methods:

- copy() - copies a set to another 
- difference() - produces the differences of two sets into a new set 
- difference_update() - this one removes the different items from the original list
- intersection() - returns the items which are present in both sets 
- intersection_update() - this one removes the items from the original set which are not same 
- isdisjoint() - returns true if none of the items match in two sets. if at least one item matches it return false
- issubset() - finds if one set is a subset of other 
- issuperset() - find if the set is a superset of other 
- symmetric_difference() - returns a set of symmetric differences of two sets 
- symmetric_difference_update() - insert the symmetric difference into the first one 
- union() - returns all items from both sets. you can pass any number of sets to union all
 
> example 1

```
pythonStudents = {'Johan','Neal','Ron','Pratyusha', 'Dia','Smyan'}
csStudents = {'Johan','Neal','Pratyusha', 'Dia','Smyan','Savita','Kalyanee'}

print("python students")
print(pythonStudents)
print("")
print("cs students")
print(csStudents)

print("")
print("common students in both classes")
tstStudents = pythonStudents.intersection(csStudents)
print(tstStudents)

print("")
print("update the cs students with those only doing python class")
csStudents.intersection_update(pythonStudents)
print("")
print("python students after update")
print(pythonStudents)
print("")
print("cs students after update")
print(csStudents)

print("")
print("Difference example")
print("")


print("")
print("even set")
evenSet = {2, 4, 6, 8, 10}
print(evenSet)

print("")
print("natural set")
naturalSet = {1,2,3,4,5,6,7,8,9,10}
print(naturalSet)

print("")
print("Difference - odd set")
oddSet = naturalSet.difference(evenSet)
print(oddSet)

print("")
print("even set")
print(evenSet)

print("")
print("natural set")
print(naturalSet)

print("")
print("Difference udpate- naural set")
naturalSet.difference_update(evenSet)
print(naturalSet)

print("")
print("even Set")
print(evenSet)

```

> example 2 - isdisjoint

```

print("")
print("even set")
evenSet = {2, 4, 6, 8, 10}
print(evenSet)

print("")
print("natural set")
naturalSet = {1,2,3,4,5,6,7,8,9,10}
print(naturalSet)

print("")
print(naturalSet.isdisjoint(evenSet))

oddSet = naturalSet.difference(evenSet)

print("")
print(oddSet.isdisjoint(evenSet))
```

> example 3 - issubset 

```

print("")
print("even set")
evenSet = {2, 4, 6, 8, 10}
print(evenSet)

print("")
print("natural set")
naturalSet = {1,2,3,4,5,6,7,8,9,10}
print(naturalSet)

print("")
print(evenSet.issubset(naturalSet))

```

> example 4 - issuperset 

```

print("")
print("even set")
evenSet = {2, 4, 6, 8, 10}
print(evenSet)

print("")
print("natural set")
naturalSet = {1,2,3,4,5,6,7,8,9,10}
print(naturalSet)

print("")
print(naturalSet.issuperset(evenSet))
```
> example 5 - symmetric_difference

```
print("even set")
evenSet = {2, 4, 6, 8, 10,12}
print(evenSet)

print("")
print("natural set")
naturalSet = {1,2,3,4,5,6,7,8,9,10}
print(naturalSet)

print("")
print(naturalSet.symmetric_difference(evenSet))
```

> example 6 - symmetric_difference_update

```

print("")
print("even set")
evenSet = {2, 4, 6, 8, 10,12}
print(evenSet)

print("")
print("natural set")
naturalSet = {1,2,3,4,5,6,7,8,9,10}
print(naturalSet)

naturalSet.symmetric_difference_update(evenSet)
print("")
print(naturalSet)

```

> example 7 - union 

```
print("")
print("even set")
evenSet = {0,2, 4, 6, 8, 10,12}
print(evenSet)

print("")
print("odd set")
oddSet = {0,1,3,5,7,9}
print(oddSet)

print("")
print("union")
print(evenSet.union(oddSet))

```

# Session work 

> ##  Predict 
what would be the output of the commmands below

```
tupleStudents = ('Johan','Neal','Ron')
tupleStudents.sort()
print(tupleStudents)

```

```
even = {2,4,6}
natural = {1,2,3,4,5,6,7}
odd = natural.difference(even)

for number in odd:
  natural.remove(number)

print(natural)
```

> ##  Investigate/Challenge
Find the problem in the code below and fix it

```
Names = {'Pratyusha', 'Ron', 'Johan', 'Dia','Smyan','Neal'}
Names.remove[3]
print(Names)

```


> ## Develop 
Write a program to accept two names. find out the below
- how many alphabets are same in both names 
- alphabets only present in first name 
- alphabets only present in second name 
- all alphabets which is not present in both names 



# Assignment
Creat three sets and without initializing, add values to all three sets. first set will be all numbers from 1 to 50, second set will be all odd numbers from 1 to 50 and the third set will be all prime numbers from 1 = 100. Then find the below :

- using set operation, find the even numbers from 1 to 50
- using set operations, find the prime numbers above 50  and less than 100 

