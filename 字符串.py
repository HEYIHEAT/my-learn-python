"""
字符串的三种定义方式:
1.单引号定义
2.双引号定义
3.三引号定义
"""
#单引号
name = 'heyi'
print(type(name))
#双引号
name = "heyi"
print(type(name))
#三引号(写法和多行注释是一样的)
#区别:如果三引号内是变量(三引号内用变量接收)则引号内自动成为字符串类型,如果不是变量则为注释
name = """
heyi
is
star
"""
print(type(name))

#在字符串内包含双引号
name = '"heyi"'
print(name)
#在字符串内包含单引号
name = "'heyi'"
print(name)
#使用转义字符 \ 解除引号的效用
name = "\"heyi\"" #即  \" 意思就是取消掉  " 的效益,将 " 当作普通字符看待(\在"前面)
print(name)
name = '\'heyi\''#注:不管如何 ,最外面都要有一个引号(最外面只能是')不能是 \'
print(name)

#字符串的拼接
print("heyi"+" is a star")#字面量之间的拼接
name = "heyi"
aka = "禾以"
print("我是:"+name+" 我的aka是:"+aka+" 我的电话是:")#字符串字面量和字符串变量的拼接
#注:加号不能将字符串和整数(110)`浮点数(3.14)等拼接起来,只能拼字符串或字符串变量

#字符串格式化(通过占位的形式,完成拼接)
name = "heyi"
message = "他们都知道:%s"%name
print(message)

class_num = 20
avg_salary = 200000
message = "heyi历史排名第%s,月薪%s"%(class_num,avg_salary)
print(message)#数字和字符串的拼接

name = "heyi"
setup_year = 2005
stock_price = 19.99
message = "有一个人%s,出生于%d,每天都以%f的倍数成长"%(name,setup_year,stock_price)
print(message)#%s是转字符串类型导入,%d是以整数类型形式导入,%f是以浮点数类型形式导入

#格式化的精度控制
num1 = 11
num2 = 11.345#小数点'.'也算一位宽度
print("数字11宽度限制5,结果:%5d"%num1)#宽度5,补了3个空格
print("数字11宽度限制1,结果:%1d"%num1)#宽度小于数字本身,无影响
print("数字11.345宽度限制7,小数精度2,结果:%7.2f"%num2)#宽度7,补了2个空格,小数精度2,四舍五入为.35
print("数字11.345不限制宽度,小数精度2,结果:%.2f"%num2)#不限制宽度,小数点后四舍五入.35

#字符串格式化方式2(字符串快速格式化)
name = "heyi"
setup_year = 2005
stock_price = 19.99
print(f"我是{name}, 我成立于{setup_year}, 我今天的股票价格是:{stock_price}")

#对表达式进行格式化
print("1*1的结果是:%d"%(1*1))
print(f"1*1的结果是:{1*1}")
print("字符串在Python中的类型是:%s"%type("字符串"))

#练习
name = "传智播客"
stock_price = 19.99
stock_code = "003032"#需要以字符串去定义,因为数字不能直接以 0 为开头
#股票价格每日增长因子
stock_price_daliy_growth_factor = 1.2
growth_days = 7

finally_stock_price = stock_price * stock_price_daliy_growth_factor**growth_days
print(f"公司:{name},股票代码:{stock_code},当前股价{stock_price}")
print("每日增长系数%.1f,经过%d天增长后,股价达到了:%.2f"%(stock_price_daliy_growth_factor,growth_days,finally_stock_price))

