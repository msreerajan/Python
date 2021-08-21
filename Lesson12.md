# Functions Exercise 

## 1. Write a Calculator program using functions to return the result based on numbers and parameters passed

# Recursive functions 

> Recursive functions are function which call itself and behave like an iteration 

```
#Fibonacci sequence using iteration
number1 = 0
number2 = 1

print(number1)
print(number2)

for i in range (0,100):
  sum = number1 + number2 
  print(sum)
  number1 = number2 
  number2 = sum
```
```
#Finonacci sequence using recursive functions 
def generateFibonacci(number1, number2):
  sum = number1 + number2
  print(sum)
  number1 = number2 
  number2 = sum 
  if number2<10000:
    generateFibonacci(number1,number2)


generateFibonacci(0,1)
```
```
#a recursive function to identify all prime numbers frmo 0 to 100
def isPrime(currentNumber, numberToCheckIfPrime ):
  if currentNumber < numberToCheckIfPrime:
    if numberToCheckIfPrime % currentNumber == 0:
      return True
    else:
      isPrime(currentNumber+1, numberToCheckIfPrime)
  else:
      return False
      
  
for i in range(2, 100):
  if not isPrime(2,i):
    print(str(i) + " Is prime")
```


# Develop

> Write following promgram using recursive Functions
- print all numbers from 0 to 100 
- print all even numbers from 0 to 100 
- accept a number from the user and check if it is prime
