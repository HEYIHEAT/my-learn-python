print("欢迎来到我的世界")
h = input("请输入你的身高(cm):")
day = input("请告诉我今天几号")
vip_level = input("请输入你的VIP级别(1~5)")
vip_level = int(vip_level)
day = int(day)
h = int(h)
if h < 120:
    print("您的身高小于120cm,可以免费游玩")
elif vip_level>3:#elif即为else if
    print("您的VIP级别大于3,可以免费游玩")
elif day==1:
    print("今天是1号免费日,可以免费游玩")
else:#也可以不写效果等同于三个独立的if判断
    print("不好意思,所有条件都不满足,需要购票10元")

print("祝您游玩愉快")
#简化代码
print("欢迎来到黑马动物园。")
if int(input("请输入你的vip级别(1-5:)")) >3:
    print("您的vip级别大于3，可以免费游玩。")
elif int(input("请输入今天的日期(1~30:)")) ==1:
    print("今天是1号免费日，可以免费游玩。")
elif int(input("请输入你的身高(cm:)")) < 120:
    print("您的身高小于120CM，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")

print("祝您游玩愉快。")
#练习
num = 10
if int(input("请输入第一次猜想的数字:")) ==num:
    print("猜对啦!")
elif int(input("不对,再猜一次:")) ==num:
    print("猜对啦!")
elif int(input("不对,再最后猜一次:")) ==num:
    print("猜对啦!")
else :print(f"Sorry!全猜错了,我想的是:{num}")

