#Practice_1
'''
Write a short program to print even numbers from 10 to 0 using a for loop.
Then use the while loop to write an equivalent program.
'''
print('Practice_1')
print('Using "for" loop')
for i in range(10, -1, -2):
    print(str(i))

print('Using "while" loop')
i = 10
while i>=0 :
    print(str(i))
    i = i-2

#Practice_2
'''
Write a short program to print a random number between 0 and 10 ten times
'''
print('Practice_2')
import random
for i in range(10):
    print(random.randint(0, 10))