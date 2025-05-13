#while循环的基础应用
i=0
while i<100:
    print("you got it!")#空格缩进与if判断一样,都需要在前面设置四个空格表示归属该while循环
    i=i+1
#练习案例:求1-100的和
i=1
sum=0
while i<=100:
    sum=sum+i
    i=i+1
print(f"1-100累加之和是:{sum}")
#while循环猜数字案例
#1.我的方法
import random
num = random.randint(1,100)
print(num)
i = 1
guess = int(input("请输入你猜测的数字:"))
if guess == num:
    print("恭喜你猜中了!")
else:
    while guess != num:
        if guess > num:
            print(f"猜的数字大了,你已猜了{i}次")
            guess = int(input("请重新输入你猜测的数字:"))
            if guess == num:
                print(f"恭喜你第{i}次猜中了!")
        elif guess < num:
            print(f"猜的数字小了,你已猜了{i}次")
            guess = int(input("请重新输入你猜测的数字:"))
            if guess == num:
                print(f"恭喜你第{i}次猜中了!")
        i = i + 1
#2.课程方法
import random#引入随机数
num = random.randint(1,100)
print(num)

count = 0#记录总共猜了几次
flag = True#通过布尔类型的变量,做循环是否继续的标记
while flag:
    guess = int(input("请输入你猜测的数字"))
    count = count + 1
    if guess == num:
        print(f"猜中了")
        flag = False
    else:
        if guess > num:
            print(f"你猜的大了")
        else:
            print(f"你猜小了")

print(f"你总共猜了{count}次")
#while循环的嵌套应用
i = 1
while i <= 100:#也需要前面四个空格缩进表示层次归属关系
    print(f"今天是第{i}天,准备表白...")
    j = 1
    while j <= 10:
        print(f"送给小美第{j}只玫瑰花")
        j = j + 1
    print("小美我喜欢你")
    i = i + 1
print(f"坚持到第{i-1}天,表白成功")#i-1:因为是i=100的情况下又一次循环+1了,所以要i-1

#补充:print不换行,制表符:\t(让多行字符串对其)=tab
print("hello")
print("world")

print("hello",end="")#end=""代表不换行 直接接着连续输出
print("world",end="")

print("hello world")
print("heyi heat")

print("hello\tworld")#'xxx\t'可以理解为将'xxx'用\t的方法做一个表格放进格子里,对齐最前面
print("heyi\theat")




#while循环案例--九九乘法表
i=1
while i <= 9:
    j=1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end="")#不换行;\t对齐
        j=j+1
    i=i+1
    print()#print空内容,就是输出换行的意思



