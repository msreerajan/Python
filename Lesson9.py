
# create a set with numbers from 1 to 50 

# create an empty set 
naturalNumbers = set()


# need numbers 1 - 50 to be added into the set 
for i in range(1,51):
  naturalNumbers.add(i)

print(naturalNumbers)

# create an empty odd number set 
oddNumbers = set()

i = 1

while i <51:
  oddNumbers.add(i)
  i+=2;

print(oddNumbers)

# create an empty set for prime numbers 

primeNumbers = set()

# all factors of the number less than the number and greater than 1, if there are no factors it will be a prime number 

# loop 1 = 100 
# in the loop - x
  # loop all the numbers from 2 to number less than the current number(x) - y 
  # divide the current number (x) by (y) == 0 
  # if it is zero the y is a factor of x, thus it is not a prime number  

