# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/24 15:23
# @Author  : Mqz
# @FileName: 12.class_1.py


# 因此我们可以在类中使用 self.WELCOME_STR ，或者在类外使用 Entity.WELCOME_STR ，
# 来表达这个字符串。
"""我们先来学习，面向对象编程中最基本的概念。为了方便你理解其中的抽象概念，我先打个比方带你
感受一下。生物课上，我们学过“界门纲目科属种”的概念，核心思想是科学家们根据各种动植物、
微生物的相似之处，将其分化为不同的类型方便研究。生活中我们也是如此，习惯对身边的事物进行分类：

猫和狗都是动物；
直线和圆都是平面几何的图形；
《哈利波特》和《冰与火之歌》（即《权力的游戏》）
都是小说。自然，同一类事物便会有着相似的特性：
动物会动；
平面图形有面积和周长；
小说也都有相应的作者和大致情节等各种元素。
"""

class Document():
    # init 表示构造函数，意即一个对象生成时会被自动调用的函数
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context  # __开头的属性是私有属性

    def get_context_length(self):
        return len(self.__context)
    # 拦截内容属性以 __ （注意，此处有两个 _）这个属性是私有属性。私有属性，是指不希望在类的函数之外的地方被访问和修改的属性
    def intercept_context(self, length):
        self.__context = self.__context[:length]

harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')

print(harry_potter_book.title)
print(harry_potter_book.author)
print(harry_potter_book.get_context_length())

harry_potter_book.intercept_context(10)

print(harry_potter_book.get_context_length())
print('*' * 10)
# print(harry_potter_book.__context)

########## 输出 ##########
#
# init function called
# Harry Potter
# J. K. Rowling
# 77
# 10
#
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-5.txt-b4d048d75003> in <module>()
#      22 print(harry_potter_book.get_context_length())
#      23
# ---> 24 print(harry_potter_book.__context)
#
# AttributeError: 'Document' object has no attribute '__context'

"""参照着这段代码，我先来简单解释几个概念。
类：一群有着相似性的事物的集合，这里对应 Python 的 class。
对象：集合中的一个事物，这里对应由 class 生成的某一个 object，比如代码中的 harry_potter_book。
属性：对象的某个静态特征，比如上述代码中的 title、author 和 __context。
函数：对象的某个动态能力，比如上述代码中的 intercept_context () 
函数。当然，这样的说法既不严谨，也不充分，但如果你对面向对象编程完全不了解，它们可以让你迅速有一个直观的了解。

可以看到，class Document 定义了 Document 类，再往下能看到它有三个函数，这三个函数即为 Document 类的三个函数。
其中，init 表示构造函数，意即一个对象生成时会被自动调用的函数。我们能看到，  harry_potter_book = Document(...)
这一行代码被执行的时候，'init function called'字符串会被打印出来。
而 get_context_length() 和 intercept_context() 则为类的普通函数，我们调用它们来对对象的属性做一些事情。
class Document 还有三个属性，title、author 和 __context 分别表示标题、作者和内容，
通过构造函数传入。这里代码很直观，我们可以看到， intercept_context 
能修改对象 harry_potter_book 的 __context 属性。这里唯一需要强调的一点是，如果一个属性以 __ （
注意，此处有两个 _） 开头，我们就默认这个属性是私有属性。私有属性，
是指不希望在类的函数之外的地方被访问和修改的属性。所以，你可以看到，title 和 author 能够很自由地被打印出来，
但是 print(harry_potter_book.__context)就会报错。
"""


class Document():
    WELCOME_STR = 'Welcome! The context for this book is {}.'

    def __init__(self, title, author, context):
        # print('init function called')
        self.title = title
        self.author = author
        self.__context = context

    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')

    # 成员函数
    def get_context_length(self):
        return len(self.__context)

    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)


empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')
# empty_book = Document.create_empty_book()
# print(empty_book.create_empty_book('hh','cc'))
print(empty_book.get_context_length())
# 也可以这样
print(Document('AA', 'BB', 'CCDDD').get_context_length())
print(Document('AA', 'BB', 'CCDDD').get_welcome('dddd'))
print(empty_book.get_welcome('indeed nothing'))

print('*'*10)
########## 输出 ##########

# init
# function
# called
# 7
# Welcome! The
# context
# for this book is indeed nothing.

"""
第一个问题，在 Python 的类里，你只需要和函数并列地声明并赋值，就可以实现这一点，
例如这段代码中的 WELCOME_STR。一种很常规的做法，是用全大写来表示常量，
因此我们可以在类中使用 self.WELCOME_STR ，或者在类外使用 Entity.WELCOME_STR ，
来表达这个字符串。而针对第二个问题，我们提出了类函数、成员函数和静态函数三个概念。它们其实很好理解，
前两者产生的影响是动态的，能够访问或者修改对象的属性；而静态函数则与类没有什么关联，最明显的特征便是，
静态函数的第一个参数没有任何特殊性。具体来看这几种函数。一般而言，静态函数可以用来做一些简单独立的任务，
既方便测试，也能优化代码结构。静态函数还可以通过在函数前一行加上 @staticmethod 来表示，代码中也有相应的示例。
这其实使用了装饰器的概念，我们会在后面的章节中详细讲解。而类函数的第一个参数一般为 cls，表示必须传一个类进来。
类函数最常用的功能是实现不同的 init 构造函数，比如上文代码中，我们使用 create_empty_book 类函数，
来创造新的书籍对象，其 context 一定为 'nothing'。这样的代码，就比你直接构造要清晰一些。类似的，
类函数需要装饰器 @classmethod 来声明。成员函数则是我们最正常的类的函数，它不需要任何装饰器声明，
第一个参数 self 代表当前对象的引用，可以通过此函数，来实现想要的查询 / 修改类的属性等功能。继承，

继承是每个富二代的梦想

接下来，我们来看第三个问题，既然类是一群相似的对象的集合，那么可不可以是一群相似的类的集合呢？
答案是，当然可以。只要抽象得好，类可以描述成任何事物的集合。当然你要小心、严谨地去定义它，
不然一不小心就会引起第三次数学危机  XD。类的继承，顾名思义，指的是一个类既拥有另一个类的特征，
也拥有不同于另一个类的独特特征。在这里的第一个类叫做子类，另一个叫做父类，特征其实就是类的属性和函数。
"""
# 类的继承，顾名思义，指的是一个类既拥有另一个类的特征，也拥有不同于另一个类的独特特征。
# 在这里的第一个类叫做子类，另一个叫做父类，特征其实就是类的属性和函数。

class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)


class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'document')
        self.title = title
        self.author = author
        self.__context = context

    def get_context_length(self):
        return len(self.__context)


class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length


harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling',
                             '... Forever Do not believe any thing is capable of thinking independently ...')
harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)

print(harry_potter_book.object_type)
print(harry_potter_movie.object_type)

harry_potter_book.print_title()
harry_potter_movie.print_title()

print(harry_potter_book.get_context_length())
print(harry_potter_movie.get_context_length())

########## 输出 ##########

"""
我们同样结合代码来学习这些概念。在这段代码中，Document 和 Video 它们有相似的地方，都有相应的标题、
作者和内容等属性。我们可以从中抽象出一个叫做 Entity 的类，来作为它俩的父类。

首先需要注意的是构造函数。每个类都有构造函数，继承类在生成对象的时候，是不会自动调用父类的构造函数的，
因此你必须在 init() 函数中显式调用父类的构造函数。它们的执行顺序是 子类的构造函数 -> 父类的构造函数。

其次需要注意父类 get_context_length() 函数。如果使用 Entity 直接生成对象，调用 get_context_length() 
函数，就会 raise error 中断程序的执行。这其实是一种很好的写法，叫做函数重写，可以使子类必须重新写一遍 
get_context_length() 函数，来覆盖掉原有函数。最后需要注意到 print_title() 函数，这个函数定义在父类中，
但是子类的对象可以毫无阻力地使用它来打印 title，这也就体现了继承的优势：减少重复的代码，降低系统的熵值（即复杂度）。

到这里，你对继承就有了比较详细的了解了，面向对象编程也可以说已经入门了。
当然，如果你想达到更高的层次，大量练习编程，学习更多的细节知识，都是必不可少的。
最后，我想再为你扩展一下抽象函数和抽象类，我同样会用一段代码来辅助讲解。

"""
# 最后，我想再为你扩展一下抽象函数和抽象类，我同样会用一段代码来辅助讲解。
from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    # 相应的抽象函数
    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title



document = Document()
document.set_title('Harry Potter')
print(document.get_title())

# entity = Entity()

########## 输出 ##########
"""你应该发现了，Entity 本身是没有什么用的，只需拿来定义 Document 和 Video 的一些基本元素就够了。
不过，万一你不小心生成 Entity 的对象该怎么办呢？为了防止这样的手误，必须要介绍一下抽象类。抽象类是一种特殊的类，
它生下来就是作为父类存在的，一旦对象化就会报错。同样，抽象函数定义在抽象类之中，子类必须重写该函数才能使用。
相应的抽象函数，则是使用装饰器 @abstractmethod 来表示。我们可以看到，代码中entity = Entity()直接报错，
只有通过 Document 继承 Entity  才能正常使用。这其实正是软件工程中一个很重要的概念，
定义接口。大型工程往往需要很多人合作开发，比如在 Facebook 中，在 idea 提出之后，
开发组和产品组首先会召开产品设计会，PM（Product Manager，产品经理） 写出产品需求文档，然后迭代；
TL（Team Leader，项目经理）编写开发文档，开发文档中会定义不同模块的大致功能和接口、每个模块之间如何协作、
单元测试和集成测试、线上灰度测试、监测和日志等等一系列开发流程。抽象类就是这么一种存在，它是一种自上而下的设计风范，
你只需要用少量的代码描述清楚要做的事情，定义好接口，然后就可以交给不同开发人员去开发和对接。
"""



