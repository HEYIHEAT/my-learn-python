print("请告诉我你是谁?")#多余
name = input()
print("Get!!你是:%s"%name)
#input语句(函数)
name = input("请告诉我你是谁?")#直接
print("Get!!你是:%s"%name)
#输入数字类型
num = input("请告诉我你的银行卡密码")#无论键盘内输入什么获取的数据永远是字符串类型
#数据类型转换
num = int(num)
print("Get!!你的银行卡密码类型是:",type(num))
#练习
user_name = input("请输入您的用户名")
user_type = input("请输入您的用户类型")
print("您好:%s,您是尊贵的%s用户,欢迎您的光临"%(user_name,user_type))