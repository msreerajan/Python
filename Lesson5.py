number = int(input("enter a number :"))#10

#i = 2 # 2---9
for i in range(2, number):
  for j in range(2, i):
    if i%j == 0:
      break
  else:
    print(str(i) + " is a prime number")
    

"""
while i<number:
  # i is the number to check if it is prime 
  # 2 and less than the number itself = 2 < n-1 
  j = 2 
  while j <i:
    if i%j == 0:
      break
    j+=1
  else:
    print(str(i) + " is prime")
  i+=1 


i=2
while i<number:
  # i is the number to check if it is prime 
  # 2 and less than the number itself = 2 < n-1 
  j = 2 
  factorFound = False
  while j <i:
    if i%j == 0:
     factorFound = True
     break
    j+=1
  if factorFound==False:
    print(str(i) + " is a prime number")
  i+=1 

"""
