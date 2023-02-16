import math

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

D = (A**2 - B**2)

ANSWER = -B + math.sqrt(D) / 2*A

print(ANSWER)

# A = math.sqrt() 5**2
# print(A)