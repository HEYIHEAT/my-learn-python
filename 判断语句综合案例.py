import random
num = random.randint(1,10)

guess = int(input("请输入你猜想的数字"))
if num == guess:
    print("恭喜你猜对啦")
else:
    if num > guess:
        print("你猜的数字小了")
    else:
        print("你猜的数字大了")

    guess = int(input("再次输入你猜想的数字"))
    if num == guess:
        print("恭喜你第二次猜对啦")
    else:
        if num > guess:
            print("你猜的数字小了")
        else:
            print("你猜的数字大了")

        guess = int(input("最后一次输入你猜想的数字"))
        if num == guess:
            print("恭喜你第三次猜对啦")
        else:
           print("三次机会用完了,没有猜中")

