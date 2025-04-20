#1.用print直接输出数据类型
print(type("我最帅"))
print(type(666))

#2.使用变量存储type()后输出
name_type = type("heyiheat")
print(name_type)

#3.查看变量中的数据存储类型信息
name = "heyiheat"
name_type = type(name)
print(name_type)

#数据类型的转换
#x转换整数:int(x) x转换浮点数:float(x) x转换字符串:str(x)
#数字转换为字符串
num_str = str(11)
print(type(num_str),num_str)

float_str = str(3.14)
print(type(float_str),float_str)
#将字符串转换成数字
num = int("11")
print(type(num),num)

num2 = float("0.11")
print(type(num2),num2)
#×错误提示:num = int("帅哥heyi") print(type(num),num)
#--该情况不成立,因为这种文字字母的字符串是不可能转化为证书或浮点数这种数字类型的
#(字符串想转换数字,必须要求字符串内的内容都是数字)

#整数转换浮点数
float_num = float(22)
print(type(float_num),float_num)

#浮点数转换整数
int_num = int(1.66)
print(type(int_num),int_num)#浮点数转换整数时小数部分(也就是精度)会丢失