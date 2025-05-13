#for循环的基础语法
name = "heyi"
for x in name:#x 即临时变量 字符串name 就是这个数据集
    #将name的内容,挨个取出赋予x临时变量
    #就可以在循环体内对x进行处理
    #(将数据集 name 中数据一个一个循环给 x (一次又一次))
    print(x)#前面也需要空格缩进
#练习案例
name = "heyi heat heyi heat heyiheyi heyiyi"
count = 0
for x in name:
    if x == "h":
        count = count + 1
print(f"被统计的字符串中,有{count}个h")
#range语句

#range语法1 range(num)--获取一个从0开始,到num结束的数字序列(不含num本身,即0-9)
for x in range(10):
    print(x)
#range语法2 range(num1,num2) ,不含num2本身
for x in range(5,10):#从5开始,到10结束(不包含10本身)
    print(x)
#range语法3 range(num1,num2,step),step:代表步长,表示数字间隔(如果不写默认为1),不含num2本身
for x in range(5,10,2):
    print(x)

for x in range(10):
    print("送玫瑰花")

#练习案例
num = int(input(f"请输入数字的变化范围1 - "))
count = 0
for x in range(1,num):
    if x % 2 == 0:
        count = count + 1
print(f"1到{num}(不包含{num}本身)范围内,有{count}个偶数")

#变量作用域
for i in range(5):
    print(i)
print(i)#在for外部,(且未定义)不符合规范,但可以运行;(解决:可以在最开始定义i=0)
#例如(正确的)
i = 0
for i in range(5):
    print(i)
print(i)#这样是规范的

#for循环的嵌套使用
i=0#提前定义一下i,让在for外部用到i时规范一些
for i in range(1,101):
    print(f"今天是向小美表白的第{i}天,坚持.")
    for j in range(1,11):
        print(f"给小妹送的第{j}朵玫瑰花")
    print("小美我喜欢你")
print(f"第{i}天,表白成功")

#for循环打印九九乘法表
#通过外层循环控制行数
for i in range(1,10):
    #通过内层循环控制每一行的数据
    for j in range(1,i+1):
        print(f"{j}*{i} = {j*i}\t",end="")

    #外层循环可以通过print输出一个回车符
    print()#print()就是回车符
