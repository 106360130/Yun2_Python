import random  #引入函式庫
import sys

print('My name is')
'''
range(start, stop, step)  //不包含"stop"，只會包含"stop"前一個 
"range()"會通常跟"for"一起搭配著使用
'''
for i in range(5):  #如果只有寫一個數字，就是"stop","start"預設為"0"
    print('Leo Five Times (' + str(i) + ')')


for i in range(5):
    #"randint()"產生範圍內隨機整數
    print(random.randint(1, 10))  #產生隨機數字的範圍是1~10

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()  #如果符合條件，程式執行就終止
    print('You typed ' + response + '.')
print('The program will never run this line')  #永遠不會執行到這行，因為在這之前程式就會終止
