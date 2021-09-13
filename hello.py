from typing import Counter


print('hello world! 你好世界')
list =["a", "b", "c"]
# 第一个注释
print (list)
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

x="a"
y="b"
# print默认换行输出
print (x)
print (y)
# 不换行输出
print (x,y)
Counter = 100
if Counter <= 100 :
    print (100)
elif Counter <= 200 :
    print(200)
else :
    print(300)
# *表示重复操作（输出次数） +表示拼接
str = 'Hello World!'
print(str[0]*2)
print(str + "TEST")  

# 无法重新赋值的元组类型
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )

# python字典（对象）

# 运算 + - * / % **(次幂) //(想下取整) and or not in not in

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('当前水果 : %s' % fruits[index])

for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)
 