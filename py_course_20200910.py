#如何取得現在".py"的檔案路徑
'''
import os
file_path = os.getcwd()  #取得當前路徑
print(file_path)
'''
file_path = 'D:\Jeff_Business\Yun2_Python\Python_Practice'  #設定路徑


passwordFile = open(file_path + '\py_course_20200910.txt')
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')



'''
Can you guess which lines of the source code are the sequence part and 
which lines of the source code are the selection part?

"sequence part" : 
只要是"指令"都算是"sequence part"，因為每一行都算是指令，因此每一行都算是"sequence part"

"selection part" : 
只要有"if、else"的部分都是"selection part"
'''
