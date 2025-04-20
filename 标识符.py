#规则1:内容限定,限定只能使用:中文、英文、数字、下划线;注意:不能以数字作为开头
#错误示范:1_name = "张三"
#错误示范:name_! = "张三"
name_ = "zhangsan"
_name = "zhangsan"
name_1 = "zhangsan"
name_2 = "zhangsan"

#规则2:大小写敏感
Heyi = "star"
heyi = "superstar"
print(Heyi)
print(heyi)

#规则3:不可使用关键字
#错误示范,使用了关键字:class = 1
#错误示范,使用了关键字:def = 1
Class = 1#大小写与关键字不同,可用