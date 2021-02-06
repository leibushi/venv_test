# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/10 14:30
# @Author  : Mqz
# @FileName: loguru_logger.py

from loguru import logger
# 基本使用
logger.debug('this is a debug message')
# 将结果输入到一个runtime。log文件里面
# logger.add('runtime.log')
logger.debug('this is a debug message')
# for x in range(1000):
#     logger.info('%s' % x)

# logger.add('runtime1.log', format="{time} {level} {message}", filter="my_module", level="INFO")
# logger.add('runtime1.log', format="{time} {level} {message}", filter="my_module", level="DEBUG")

from loguru import logger

trace = logger.add('runtime2.log')
logger.debug('this is a debug message11')
# logger.remove(trace)
# logger.debug('this is another debug message11')

# rotation 配置
# 通过这样的配置我们就可以实现每 500MB 存储一个文件，每个 log 文件过大就会新创建一个 log 文件。我们在配置 log
#  名字时加上了一个 time 占位符，这样在生成时可以自动将时间替换进去，生成一个文件名包含时间的 log 文件。
# logger.add('runtime_{time}.log', rotation="1024 MB")
# 配置为1k大的文件
# logger.add('runtime_{time}.log', rotation="1024 B")
# logger.add('runtime_{time}.log', rotation="10 MB")
# logger.info()
# for x in range(10000000000000):
#     logger.info('%s' % x)

# 另外我们也可以使用 rotation 参数实现定时创建 log 文件，例如：
# 这样就可以实现每天 0 点新创建一个 log 文件输出了。
# logger.add('runtime_{time}.log', rotation='16:13')
# 另外我们也可以配置 log 文件的循环时间，比如每隔一周创建一个 log 文件，写法如下：

# logger.add('runtime_{time}.log', rotation='1.txt week')

# retention 配置
# 很多情况下，一些非常久远的 log 对我们来说并没有什么用处了，它白白占据了一些存储空间，
# 不清除掉就会非常浪费。retention 这个参数可以配置日志的最长保留时间。
# logger.add('runtime.log', retention='10 days')

# compression 配置
# loguru 还可以配置文件的压缩格式，比如使用 zip 文件格式保存，示例如下：

# logger.add('runtime.log', compression='zip')

# 字符串格式化
# loguru 在输出 log 的时候还提供了非常友好的字符串格式化功能，像这样：

logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
@logger.catch()
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)

my_function(0, 0, 0)