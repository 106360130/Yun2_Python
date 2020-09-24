#Q1
'''
"statement"是命令，只要輸入指令就執行
"expression"是計算，有兩個或兩個以上的變數作運算
"expression"會產出"數值"，但"statement"不會產出數值
最簡單的判斷就是在終端機測試(先下"py -3"指令)，打要測試的"程式"

e.g.
print("123") 
print(5)
以上兩行都有輸出"值"
(在此指的"值"不一定是數字也可以是"字串"，只要有輸出出來都算是"值")
'''

#Q2
bacon = 101
print('bacon : ' + str(bacon))
bacon + 1  #因為只有加但最後並沒有儲存在"bacon"裡


#Q3
print('bacon : ' + str(bacon))
ans = 'I have eaten ' + str(99) + ' burritos.'   #"99"必須強制轉型成str
print(ans)


#practice
result = (2**13 * 313 + 1) / 7
print(result)
