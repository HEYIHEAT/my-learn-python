#定义变量
#情况一
age = 30
print(f"今年我已经{age}岁了")
#进行判断
if age >= 18:
    print("我已经成年了")#前面留四个空格缩进表示归属if
    print("即将步入大学生活")

print("时间过得真快")#前面没有留四个空格缩进,不受if限制
#情况二
age = 10
print(f"今年我已经{age}岁了")
# 进行判断
if age >= 18:
    print("我已经成年了")  # 前面留四个空格缩进表示归属if
    print("即将步入大学生活")

print("时间过得真快")  # 前面没有留四个空格缩进,不受if限制

#练习
print("欢迎来到我的世界,儿童免费,成人收费")
age_play = input("请输入你的年龄:")
age_play = int(age_play)
#必须需要这一步,因为input会把任何数据变成字符串类型,而下面的if判断条件可以看出是需要整数类型int的
if age_play >= 18:
    print("您已成年,游玩需补票10元")

print("祝您玩的愉快")