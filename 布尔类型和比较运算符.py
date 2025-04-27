#布尔类型的数据,不仅可以通过定义得到,也可以通过 比较运算符 进行内容比较得到
#定义变量存储布尔类型的数据
bool1 = True
bool2 = False
print((bool1,bool2),f"bool1变量的内容是:{bool1},类型是:{type(bool1)}")
print(((bool1,bool2)),f"bool2变量的内容是:{bool2},类型是:{type(bool2)}")
#比较运算符来表示(==,!=,<,>,>=,<=)
num1 = 10
num2 = 5
result = num1>num2
print(f"10>5的结果是:{result},类型是{type(result)}")
result = "heyi"=="heyiheat"
print(f"字符串heyi是否和heyiheat相等,结果是:{result},类型是{type(result)}")
