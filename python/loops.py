'''
Types of loops:
- for loop 
- while loop

Three requirements for a loop:
- Iterator
- Condition
- Increment/Decrement
'''

i = 1

while i <= 10:
    print(i)
    i += 1 #i = i + 1

#range(start=0, stop, step=1)
for i in range(1, 11):
    print(i)