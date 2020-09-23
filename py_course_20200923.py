#What do the following expressions evaluate to?

#Q1 not True and (True or False)
ans_1 = (not True and (True or False))
print("ans_1 : ", ans_1)
'''
有"括弧"的優先序比較高
1. ((not True) and (True or False))
2. ((not True) and (True))
3. (False and True)
4. (False)
'''

#Q2 5 == 4 or not 5 < 10 or not 3 >= 3
ans_2 = (5 == 4 or not 5 < 10 or not 3 >= 3)
print("ans_2 : ", ans_2)
'''
5 == 4  //False
5 < 10  //True
3 >= 3  //True

1. (5 == 4 or not 5 < 10 or not 3 >= 3)
2. (False or not True or not True)
3. (False or (not True) or (not True))
4. (False or (False) or (False))
5. (False)
'''