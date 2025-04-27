print("欢迎来到我的世界,儿童免费,成人收费")
age_play = input("请输入你的年龄:")
age_play = int(age_play)
#必须需要这一步,因为input会把任何数据变成字符串类型,而下面的if判断条件可以看出是需要整数类型int的
if age_play >= 18:
    print("您已成年,游玩需补票10元")
else:
    print("您未成年,可以免费游玩")# 前面留四个空格缩进表示归属else

print("祝您游玩愉快")
#练习
print("欢迎来到我的世界")
h = input("请输入你的身高:")
h = int(h)
if h >= 120:
    print("您的身高超出120cm,游玩需要购票10元")
else:
    print("您的身高未超出120cm,可以免费游玩")

print("祝您游玩愉快")
