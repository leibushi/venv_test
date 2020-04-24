# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 9:40
# @Author  : Mqz
# @FileName: 9.try_except.py

try:
    s = input('please enter two numbers separated by comma:')
    num = s.split(',')  # ['12', '45']
    nums = s.split(',')[0]  # ['12', '45']
    print(nums)
    num1 = int(s.split(',')[0].strip())
    print(num1)
    num2 = int(s.split(',')[1].strip())
    print(num2)
    print(type(num2))

except IndexError as err:
    print('IndexError: {}'.format(err))

except ValueError as err:
    print('Value Error: {}'.format(err))

print('continue')

"""
# try:的两种写法
方法1
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except (ValueError, IndexError) as err:
    print('Error: {}'.format(err))

print('continue')

# 方法二

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))

print('continue')

每次程序执行是，except block中只有一个exception类型与实际匹配即可。
很多时候，我们很难保证程序覆盖所有的异常类型，所以，更通常的做法，是在最后一个 except block，
声明其处理的异常类型是 Exception。Exception 是其他所有非系统异常的基类，能够匹配任意非系统异常
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except Exception as err:
    print('Other error: {}'.format(err))

print('continue')

或者，你也可以在 except 后面省略异常类型，这表示与任意异常相匹配（包括系统异常等）：

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except:
    print('Other error')

print('continue')
需要注意，当程序中存在多个 except block 时，最多只有一个 except block 会被执行。换句话说，
如果多个 except 声明的异常类型都与实际相匹配，那么只有最前面的 except block 会被执行，其他则被忽略。
...
"""

# 异常处理中，还有一个很常见的用法是 finally，经常和 try、except 放在一起来用。无论发生什么情况，
# finally block 中的语句都会被执行，哪怕前面的 try 和 excep block 中使用了 return 语句。

# 一个常见的应用场景，便是文件的读取：

# import sys
# try:
#     f = open('file.txt', 'r')
#     # some data processing
# except OSError as err:
#     print('OS error: {}'.format(err))
# except:
#     print('Unexpected error:', sys.exc_info()[0])
# finally:
#     # 在 finally 中，我们通常会放一些无论如何都要执行的语句。
#     f.close()

"""
值得一提的是，对于文件的读取，我们也常常使用 with open，
你也许在前面的例子中已经看到过，with open 会在最后自动关闭文件，让语句更加简洁
"""

# 用户自定义异常

class MyInputError(Exception):
    """Exception raised when there're errors in input"""

    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value

    def __str__(self):  # 自定义异常类型的string表达形式
        print(repr(self.value))
        return ("{} is invalid input".format(repr(self.value)))


try:
    raise MyInputError(1)  # 抛出MyInputError这个异常
except MyInputError as err:
    print('error: {}'.format(err))
    
    
"""repr(object)
参数
object -- 对象。
返回值
返回一个对象的 string 格式。
"""

# 而数据库返回的原始数据，往往是 json string 的形式，这就需要我们首先对 json string 进行
# decode（解码），你可能很容易想到下面的方法：

"""
import json
# raw_data = queryDB(uid) # 根据用户的id，返回相应的信息
raw_data = {'xx': {}}
# 不应该这样
data = json.loads(raw_data)
# 应该这样
try:
    data = json.loads(raw_data)
    print(data)
except JSONDecodeError as err:
    print('JSONDecodeError: {}'.format(err))
"""

# 不能滥用异常处理
# 比如，当你想要查找字典中某个键对应的值时，绝不能写成下面这种形式：

d = {'name': 'jason', 'age': 20}
# try:
#     value = d['dob']
#     ...
# except KeyError as err:
#     print('KeyError: {}'.format(err))

# 诚然，这样的代码并没有 bug，但是让人看了摸不着头脑，也显得很冗余。如果你的代码中充斥着这种写法，无疑对阅读、
# 协作来说都是障碍。因此，对于 flow-control（流程控制）的代码逻辑，我们一般不用异常处理。
# 写成这样就好了
if 'dob' in d:
    value = d['dob']
    print(value)
    ...
print(d)

"""异常，通常是指程序运行的过程中遇到了错误，终止并退出。我们通常使用 try except 语句去处理异常，
这样程序就不会被终止，仍能继续执行。处理异常时，如果有必须执行的语句，比如文件打开后必须关闭等等，则可以放在 finally  block 中。异常处理，通常用在你不确定某段代码能否成功执行，也无法轻易判断的情况下，
比如数据库的连接、读取等等。正常的 flow-control 逻辑，不要使用异常处理，直接用条件语句解决就可以了。
"""

# test

# 第一种


try:
    db = DB.connect('<db path>') # 可能会抛出异常
    raw_data = DB.queryData('<viewer_id>') # 可能会抛出异常
except (DBConnectionError, DBQueryDataError) err:
    print('Error: {}'.format(err))

# 第二种

try:
    db = DB.connect('<db path>') # 可能会抛出异常
    try:
        raw_data = DB.queryData('<viewer_id>')
    except DBQueryDataError as err:
         print('DB query data error: {}'.format(err))
except DBConnectionError as err:
     print('DB connection error: {}'.format(err))