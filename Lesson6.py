"""
numberOfLines = int(input("how many lines do you want? "))
i = 1

while i <= numberOfLines:
  for j in range(i):
    #print("i = " + str(i) + ", j= " + str(j))
    print('* ', end="")
  i+=1
  print(i)
"""

for i in range(5):
  for j in range(i):
    #print('* ', end="")
    print("i " + str(i) + ", j =" + str(j))
