print("欢迎来到黑马动物园。")
if int(input("请输入你的身高(cm):"))>120:
    print("你的身高大于120cm,不可以免费")
    print("不过如果你的VIP等级高于3,可以免费游玩")
    if int(input("请告诉我你的VIP等级"))>3:#嵌套关键点在于:空格缩进
        print("恭喜你!VIP等级大于3,可以免费游玩")
    else:#通过空格缩进来决定语句之间的:层次关系
        print("sorry,你需要补票10元")
else:
    print("你可以免费游玩")

#2
age = int(input("请输入你的年龄"))
wrok_time = int(input("请输入你的入职时间(年)"))
level = int(input("请输入你的级别"))
if age>=18:
    print("成年人符合,继续判断")
    if age<30:
        print("年龄达标继续判断")
        if wrok_time>2:
            print("小于30岁的成年人且入职超过2年,满足条件可以领取")
        elif level>3:
            print("级别大于3的成年人可直接领取礼物")
        else:
            print("您的年龄符合,但入职时间不足且级别小于3,不可领取")
    else:
        print("不好意思,年龄太大了,不可以领取")
else :
    print("未成年人不可领取")