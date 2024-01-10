---
layout: post
title: "python进阶-01"
date: 2023-08-09  
tags: [python]
---

### [**back**](../index.md)   |   [**code**](https://github.com/JW-Zhang001/Blog-code/tree/main/python/python-code) 


## 1.基础知识

### 1.1 变量赋值和引用

- 每定义一个新变量时,就会在内存中开辟一块空间用于数据存储。不同的变量,内存地址是不同的。
- 使用 `id()` 获取内存地址，使用 `is` 判断变量内存地址是否相同。

1. 把一个变量的内存地址同时关联到另一个变量上,称为引用。两个变量对应同一块内存地址

   ```python
    a = 100
    b = a
    assert id(a) == id(b)
    assert a is b
   ```

2. 不可变类型变量和可变类型变量在引用时的区别

   常用int、字符串都是不可变类型, 字典、集合、列表都属于可变类型的变量

   ```python
   # b引用a所指向的数据
   a = 100
   b = a
   assert id(a) == id(b)
   assert a is b
   
   a = 100
   b = a
   a = 200
   print(a, b)  # 200 100
   assert a is not b
   assert id(a) != id(b)
   
   a1 = "str"
   b1 = a1
   a1 = "string"
   print(a1, b1)  # string str
   
   a = [1, 2, 3, 4]
   b = a
   a[0] = 100
   print(a[0], b[0])  # 100, 100
   assert a is b
   assert id(a) == id(b)
   ```

   

### 1.2 小整数池和字符串驻留

Python中存在一个小整数池，范围通常在-5到256之间。在这个范围内的整数会被提前创建并缓存，以便节省内存。    

字符串驻留范围:英文字母、数字、下划线

**以下代码在Ipthon中执行,使用Vscode和PythonCharm执行结果可能不同**

```python
# 在ipython中执行
a = 100
b = 100
print(a is b)  # True

a = 500
b = 500
print(id(a) == id(b))  # False

a, b = 500, 500
print(a is b) # True 一行定义两个相同值的变量,解释器会优化,a、b是同一内存地址

a = "abc"
b = "abc"
print(a is b)  # True

a = "abc!"
b = "abc!"
print(a is b)  # False
```


### 1.3 数据类型

数值: int float bool complex(复数)  
序列: str list tuple  
散列: set dict  

- 常见基础面试题

  - 列表去重方案

    ```python
    # 方案一  set() 利用集合去重的特性
    original_list = [1, 2, 3, 4, 3, 2, 1]
    deduplicated_list = list(set(original_list))
    print(deduplicated_list)  # 输出: [1, 2, 3, 4]
    
    # 方案二  使用enumerate 找到列表下标判断元素是否存在
    deduplicated_list = [x for i, x in enumerate(original_list) if x not in original_list[:i]]
    print(deduplicated_list)  # 输出: [1, 2, 3, 4]
    
    # 方案三  使用 dict.fromkeys():利用字典的键的唯一性
    deduplicated_list = list(dict.fromkeys(original_list))
    print(deduplicated_list)  # 输出: [1, 2, 3, 4]
    
    # 方案四  使用 Counter 是 collections 模块提供的一个计数器对象，可以用来统计元素出现的次数
    deduplicated_list = list(Counter(original_list)) # Counter({1: 2, 2: 2, 3: 2, 4: 1})
    print(deduplicated_list)  # 输出: [1, 2, 3, 4]
    ```

  - 字符串反转

    ```python
    print("第一种方式:", "".join(reversed(data)))
    
    print("第二种方式:", data[::-1])
    ```

- 推导式

  list推导式

  ```python
  result = ["data{}".format(i) for i in range(0, 100) if i % 2 == 0]
  ```

  dict 推导式

  ```python
  print({f"data{(i + 1)}": i + 1 for i in range(3)})  # {'data1': 1, 'data2': 2, 'data3': 3}
  ```

  set 推导式

  ```python
  { expression for item in Sequence if conditional }
  ```

  tuple 推导式 （生成器表达式）

  ```python
  a = (x for x in range(1,10))  # <generator object <genexpr> at 0x7faf6ee20a50>  生成器对象
  tuple(a)  # 使用 tuple() 函数，可以直接将生成器对象转换成元组
  ```



### 1.4 collections

>  这个模块实现了一些专门化的容器，提供了对 Python 的通用内建容器 dict、list、set 和 tuple 的补充。

```python
from collections import namedtuple, deque, ChainMap

# namedtuple 命名元祖
Student = namedtuple('Students', ["name", "age", 'index'])
tu1 = Student(name="张三", age=18, index=1)
print(tu1.name)  # 张三
print(isinstance(tu1, tuple))  # True 也是元祖类型数据
print(type(tu1))  # tu1数据类型 <class '__main__.Students'> Student对象
```

```python
# deque 双端队列
d = deque('ghi')
d.extendleft('123', )
d.appendleft('4')
print(d)   # deque(['4', '1', '2', '3', 'g', 'h', 'i'])
```

```python
# ChainMap 将多个字典或者其他映射组合在一起，创建一个单独的可更新的视图
dict1 = {'music': 'bach', 'art': 'rembrandt'}
dict2 = {'art': 'van gogh', 'opera': 'carmen'}
dict3 = {'opera': 'dict3', 'test': 'dict3'}
c = ChainMap(dict1, dict2, dict3)
# 获取map中的key和其传入参数有关系, 迭代顺序是通过从后往前扫描
print(c.get('art'), c.get('opera'))  # rembrandt, carmen
# 如果要实现dict.update功能,可以使用update()
c.update(dict3)
print(c.get('art'), c.get('opera'))  # rembrandt, dict3
```



### 1.5 iterable

**可迭代对象: 可被 for 遍历都是可迭代对象**  

1. 实现了 __iter__ 方法，并且该方法返回一个迭代器对象。  
2. 实现了 __getitem__ 方法，并且可以通过索引访问元素。

> *class* collections.abc.**Iterable**
>
> 提供了 `__iter__()` 方法的抽象基类。
>
> 使用 `isinstance(obj, Iterable)` 可以检测一个类是否已经注册到了 [`Iterable`](https://docs.python.org/zh-cn/3/library/collections.abc.html?highlight=iterable#collections.abc.Iterable) 或者实现了 `__iter__()` 函数，但是无法检测这个类是否能够使用 `__getitem__()` 方法进行迭代。检测一个对象是否是 [iterable](https://docs.python.org/zh-cn/3/glossary.html#term-iterable) 的唯一可信赖的方法是调用 `iter(obj)`。

示例1: 实现 `__iter__` 但是返回一个list 非迭代器对象  

```python
class Iterable1:
    def __init__(self):
        self.data = [1, 2, 3, 4]

    def __iter__(self):
        # 返回的是一个列表,而不是一个迭代器对象
        return self.data


obj1 = Iterable1()
assert isinstance(obj1, Iterable)  # True
assert iter(obj1)  # iter() returned non-iterator of type 'list'
```

示例2: 实现 `__iter__` 返回一个迭代器对象  

```python
class Iterable2:
    def __init__(self):
        self.data = [1, 2, 3, 4]

    def __iter__(self):
        # 返回的是一个迭代器对象
        return iter(self.data)

obj2 = Iterable2()  # obj2 是可以被for遍历的对象
print(iter(obj2)) # <list_iterator object at 0x1043bb6d0>
```

示例3: 实现 `__getitem__` 访问元素  

```python
class Iterable3:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __getitem__(self, index):
        # 通过索引访问元素，实现迭代行为
        return self.data[index]

my_iterable = Iterable3()
print(iter(my_iterable))
```



### 1.6 iterator

**迭代器:必须要同时拥有 `__iter__` 和 `__next__` 方法才是迭代器**

> 迭代器调用 `__next__` 方法会调用迭代器中的下一个值

示例1:通过 iter(iterable) 得到迭代器

```Python
my_iterator = iter(["1", "2", "3"])
# hasattr 判断某个对象是否包含某个属性信息
print(hasattr(my_iterator, "__iter__"))  # True
print(hasattr(my_iterator, "__next__"))  # True
```

示例2:实现一个迭代器，必须要实现 `__next__` 和 `__iter__` 方法

> 示例中并没有手动实现 `__iter__` 会使用父类的 `__iter__` 

```Python
from typing import Iterator


class Students(Iterator):
    def __init__(self):
        self.students = ["张三", "李四", "王五"]
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        self.index += 1
        return self.students[self.index - 1]


print(isinstance(Students(), Iterator))  # True
print(my_iterator.__iter__())  # <__main__.Students object at 0x1009a7950>
for item in Students():
    print(item)  
```

示例3:实现一个迭代器，自己实现 `__init__` 方法

```python
class Students2(Iterator):
    def __init__(self):
        self.students = ["1", "2"]
        self.index = 0

    def __iter__(self):
        return iter(self.students)

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        self.index += 1
        return self.students[self.index - 1]


my_iterator2 = Students2()
print(my_iterator2.__iter__())  # <list_iterator object at 0x104f37fd0>
print(isinstance(my_iterator2, Iterator))  # True
print(next(my_iterator2))  # 1
print(next(my_iterator2))  # 2
print(next(my_iterator2))  # raise StopIteration
```

示例4:实现一个 range 迭代器

> 1. range 方法的签名 start、stop 两个参数
> 2. `__iter__` 方法要求返回值必须是一个”迭代器“ (或者返回值必须要有 `__next__` 方法)

```python
class Next:
    def __init__(self, stop, start=-1):
        self.start = start
        self.stop = stop

    def __next__(self):
        if self.start >= self.stop - 1:
            raise StopIteration
        self.start += 1
        return self.start


class MyRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return Next(self.stop)


my_range = MyRange(5)  # <__main__.MyRange object at 0x1045029d0>
# False 断言它不是一个迭代器,但是它可以被for遍历,所以__iter__返回值有__next__方法也可以
print(isinstance(my_range, Iterator)) 
for item in my_range:
    print(item)  # 也可以通过 for 遍历
```

示例5: 基于MyRange使用while实现for 

> for 会自动调用 `__iter__` , `__next__` 方法,但是while不会,需要手动调用

```python
# 基于MyRange使用while实现for
def my_while():
    start, stop = 0, 5
    my_range = MyRange(stop)
    numbers = my_range.__iter__()  # 手动调用__iter__方法
    while start < stop:
        print(numbers.__next__())
        start += 1


my_while()
```



### 1.7 generator

**生成器(高效):生成器是特殊的迭代器,迭代器是特殊的可迭代对象,那么生成器必定是可迭代对象**

> 使用yield关键字返回一个生成器对象

```Python
from typing import Iterable, Iterator


def g_func2():
    my_list = range(3)
    for i in my_list:
        yield i * i


g = g_func2()

print(isinstance(g, Iterable))  # True
print(g.__iter__())  # <generator object g_func1 at 0x10271fc10>
print(next(g))
print(next(g))
print(next(g))
print(hasattr(g, "__iter__"))  # True
print(hasattr(g, "__next__"))  # True
print(isinstance(g, Iterator))  # True
```



### 1.8 for循环的本质

> 1. 调用iter()，将numbers转化为迭代器numbers_iterator
> 2. 调用next(numbers_iterator)，返回出numbers的第一个元素
> 3. 循环步骤2,迭代完numbers内所有数据,捕获异常

```python
# while + iterator
numbers = [1, 2, 3, 4]
numbers_iterator = iter(numbers)
while True:
    try:
        print(next(numbers_iterator))
    except StopIteration:  # 捕捉异常终止循环
        break

# for循环
for i in numbers:
    print(i)
```



### 1.9 itertools

> 为高效循环而创建迭代器的函数

```Python
iterable = itertools.chain(["A", "B", "C"], ["D", "E", "F"])
for i in iterable:
    print(i)  # --> A B C D E F

from_iterable = itertools.chain.from_iterable(['ABC', 'DEF'])
for i in from_iterable:
    print(i)

r = itertools.combinations("ABCD", 2)
for i in r:
    print(i)  # --> AB AC AD BC BD CD
```



### 1.10 lambda、map、zip

- lamdba 处理简单业务逻辑

  ```python
  y: any = lambda x: x + 1
  print(y(10))
  
  Students = [
      {"name": "a", "age": 18},
      {"name": "c", "age": 20},
      {"name": "b", "age": 19},
      {"name": "ca", "age": 19},
      {"name": "cb", "age": 19}
  ]
  # 根据age排序,age一致时根据name排序
  print(sorted(Students, key=lambda student: (student["age"], student["name"])))
  ```

- map(func, *iterables) --> map object

  ```python
  # map 可迭代对象元素合并 返回新的map对象,按最短的对象合并
  a = [1, 2, 3]
  b = [4, 5, ]
  # map(func, *iterables)
  # func --> lambda a1, b1: (a1, b1)
  # *iterables --> a, b
  num1 = map(lambda a1, b1: (a1, b1), a, b)  # <map object at 0x109efed60>
  for i in num1:
      print(i)  # (1, 4), (2, 5)
  ```

- reduce 求和

  ```Python
  from functools import reduce
  print(reduce(lambda x, y: x + y, range(1, 101)))  # 5050
  ```

- filter 过滤

  ```python
  print(list(filter(lambda x: x > 5, range(10))))  # <filter object at 0x106ad6c40>
  ```

- zip

  ```python
  a = [1, 2, 3]
  b = [4, 5, 6, 7, 8]
  print(list(zip(a, b)))  # [(1, 4), (2, 5), (3, 6)]  # 元素个数与最短的列表一致
  ```



### 1.11 namespace

- 一般有三种命名空间:
  1. 内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
  2. 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
  3. 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

- Python的作用域一共有4种【规则顺序: L –> E –> G –> gt; B】

  1. L（Local）:最内层，包含局部变量，比如一个函数/方法内部。

  2. E（Enclosing）:包含了非局部(non-local)也非全局(non-global)的变量。

     比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。

  3. G（Global）:当前脚本的最外层，比如当前模块的全局变量。

  4. B（Built-in）: 包含了内建的变量/关键字等。最后被搜索



- 闭包

  > 1.在一个函数内部定义了另一个函数  
  > 2.内部函数引用了外部函数的变量

  ```python
  g_count = 0  # 全局作用域
  
  
  def outer():
      o_count = 1  # 闭包函数外，函数中
      print(f"Enclosing: {o_count}")
  
      def inner():
          i_count = 2  # 局部作用域
          print(f"Local: {i_count}")
          nonlocal o_count  # 外层作用域
          o_count += 5
          print(f"Enclosing: {o_count}")
  
      return inner  # 返回函数名称 可以被调用
  
  
  print(f"Global: {g_count}")  # Global: 0
  func = outer()  # Enclosing: 1
  func()  # Local: 2 Enclosing: 6
  func()  # Local: 2 Enclosing: 11
  ```



### 1.12 private_name

```python
# import 私有变量
# 1. __name它不会被导入到导入模块的命名空间中
# 2. _name会被导入到导入模块的命名空间中
```

```python
class MyClass:
    def __init__(self):
        self.__name = "Private Name"  # 私有变量 __name
        self._name = "Conventionally Private Name"  # 约定上的私有变量 _name

    def get_private_name(self):
        return self.__name

    def get_conventionally_private_name(self):
        return self._name


obj = MyClass()

# 访问私有变量 __name
print(obj.get_private_name())  # 输出: Private Name
# print(obj.__name)  # 错误，在类外部，无法直接访问私有变量，会引发 AttributeError 错误
print(obj._MyClass__name)  # 输出: Private Name，通过名称重整方式访问私有变量

# 访问约定上的私有变量 _name
print(obj.get_conventionally_private_name())  # 输出: Conventionally Private Name
print(obj._name)  # 输出: Conventionally Private Name，可以直接访问约定上的私有变量
```



## 2.装饰器(decorator)

> 本质函数当作参数传递,利用闭包特性实现



### 2.1 最原始的装饰器

```Python
def add(*args):
    return sum(args)


# 把函数当做参数,传递给另外一个函数
def new_add(func, *args):
    return f"对原函数进行装饰 遵循开放封闭原则: {func(*args)}"


print(new_add(add, 1, 2, 3))
```



### 2.2 常见使用方式

> 编写一个记录日志 和 统计函数执行耗时的装饰器

```python
import time


def loger(func):
    def wrapper(*args):
        print("1 记录日志的代码...")
        result = func(*args)
        print("2 日志分析的代码...")
        return result

    return wrapper


# 编写一个计算方法执行耗时的装饰器
def timer(func):
    def wrapper(*args, **kwargs):
        print("3 计算耗时开始")
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"{func.__name__}: 耗时: {end_time - start_time}")
        print("4 计算耗时结束")
        return result

    return wrapper


@loger
@timer
def add(*args, **kwargs):
    return sum(args)


print(add(11, 1))  # 执行顺序: 1 -> 3 -> func.__name__耗时 -> 4 -> 2 -> func执行结果
```



### 2.3 装饰器带参数

```python
# 编写一个带参数的装饰器，用于验证用户登录
def login_verify(is_login=False):  # 这里接收装饰器的参数
    def inner(func):  # 接收被装饰的函数
        def wrapper(*args, **kwargs):  # 这里接收被装饰函数的参数
            if is_login:  # 装饰器的参数在这里使用，用于判断
                print("被装饰函数执行前")
                result = func(*args)
                print("被装饰函数执行后")
                return result
            else:
                return None

        return wrapper  # 返回函数的包装器

    return inner


@login_verify(is_login=True)
def add(*args, **kwargs):
    return sum(args)


print(add(11, 22))
```



### 2.4 给类添加一个装饰器

```python
def class_name(cls):
    cls.name = "小明"
    return cls

# 给类添加装饰器
@class_name
class A(object):
    pass


print(A.name)
```



### 2.5 使用类编写装饰器

```python
class A:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("__call__ is running ...")
        return self.func(*args)


@A  # 本质 A(add)
def add(*args):
    return sum(args)


print(add(1, 2))
```



### 2.6 使用类编写装饰器带参数

```python
class S:
    def __init__(self, func, name):
        self.func = func
        self.name = name

    def __call__(self, *args, **kwargs):
        print("类装饰器转入的参数", self.name)
        print("1 装饰函数执行之前")
        result = self.func(*args)
        print("2 装饰函数执行之后")
        return result


def add(*args):
    return sum(args)


s = S(add, "hello")
print(s(1, 3))
```



## 3.面向对象

### 3.1 三大特性

> 面向对象三大特性:继承 封装 多态

```python
# 面向对象三大特性:继承 封装 多态
class Base(object):
    def __init__(self):
        self.leg = "4"

    def func1(self):
        print(f"Base 有 {self.leg} 条腿...")


class Cat(Base):
    def func1(self):
        print(f"我是cat,有{self.leg}条腿...")
        print("我会上树")


class Dog(Base):
    def func1(self):
        print(f"我是dog,有{self.leg}条腿...")
        print("我跑得快")


class Table(Base):
    def func1(self):
        print(f"我是一个餐桌，也有{self.leg}条腿，但我不会跑...")


def func(arg):
    arg.func1()


func(Base())
func(Dog())
func(Cat())
func(Table())
```



### 3.2 类方法和静态方法

> classmethod 给类定义的方法
> staticmethod 目的只是封装在一起,内聚

```python
class Person(object):

    def __init__(self, name):
        self.name = name

    @classmethod
    def name(cls, name):
        return cls(name)

    @staticmethod
    def age(age: int):
        return age

    def __repr__(self):
        return self.name


a = Person(name="张三")
print(a)
b = Person.name("李四")
print(b)
print(a.age(18))  # 对象可以调用
print(Person.age(20))  # 类也可以调用
```



### 3.3 property装饰器

> 1.将函数属性伪装成数据属性
> 2.统一数据属性的查、改、删操作

```python
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    # 当name 遇到赋值操作, 即 = 时触发被property.setter装饰的函数的执行
    @name.setter
    def name(self, value):
        self.__name = value

    # 当name 遇到删除操作，即 del 时触发property.deleter装饰的函数的执行
    @name.deleter
    def name(self):
        print('deleter')


obj1 = Person('abc')
print(obj1.name)
obj1.name = 'aaa'
print(obj1.name)
del obj1.name
```



### 3.4 cached_property 

> 相比 `property` 增加缓存功能,针对不可变的高计算资源消耗的实例特征属性

```python
from functools import cached_property  # 内置 3.8版本才加入的cached_property
pip3 install cached-property  # 第三方包 支持asyncio
```



### 3.5 属性查找顺序

> 对象 --->   父类   --->    继承类,  依次类推,找不到则报错



### 3.6 多继承

- 多继承的优点:同时继承多个父类属性和方法，功能强大。
- 多继承缺点:代码可读性变差。
- 通过类的mro()方法查看多继承的查找顺序。
- `__bases__` 可以查看类继承的所有父类

~~~python
print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(C.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>)
~~~



### 3.7 广度优先和深度优先

```python
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.A1'>, <class '__main__.B'>, <class 'object'>]

# python3中全部默认继承object，所以都是新式类
- object类提供了一些常用内置方法的实现,如用来在打印对象时返回字符串的内置方法__str__

新式类:广度优先
obj -> <class '__main__.C'> -> <class '__main__.A1'> ... -> <class 'object'>
```



### 3.8 抽象基类

> 1.抽象类本身不能实例化
>
> 2.子类必须实现其定义接口

```python
import abc


# 指定metaclass属性将类设置为抽象类，抽象类本身不能实例化
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 该装饰器限制子类必须定义有一个名为talk的方法
    def talk(self):  # 抽象方法中无需实现具体的功能
        pass


class Cat(Animal):  # 但凡继承Animal的子类都必须遵循Animal规定的标准
    def talk(self):  # 必须定义talk方法						
        pass


cat = Cat()  # 若子类中没有一个定义talk的方法则会抛出异常TypeError，无法实例化
```



### 3.9 isinstance 和 issubclass

```python
print(isinstance(a, int))  # 断言类型
print(issubclass(People, Animal))   # 断言是否其子类
```



### 3.10 动态获取对象信息(反射)

```python
hasattr(obj, 'x')	                    # 判断对象是否有一个属性，返回布尔值
getattr(object, name, default=None)	  # 获取对象的name属性，name属性不存在的返回None
setattr(x, 'y', 'v')	       # 更新x对象 y属性的值, 等价于 x.y = 'v'，当y不存在的新增
delattr(x, 'y')		           # 删除x对象 y属性, 等价于 del x.y   属性y不存在则报错
```



## 4.魔法函数

### 4.1 `__new__` 、`__init__` 、`__call __`、`__del__`

> `__new__`       实例化对象（1.创建对象 2.分配内存）
> `__init__`    构造方法,实例化对象时自动调用(1.可以没有 2.如果有方法必须返回None,默认不写return语句)
> `__call __`  对象可以被调用时触发执行
> `__del__`      析构方法,当对象被回收时触发执行(程序结束、对象引用计数为零称为垃圾时)

```python
class MyClass(object):

    def __init__(self):
        print("__init__ is running...")

    def __new__(cls):
        print("__new__ is running...")
        return super().__new__(cls)  # 创建对象 分配内存

    def __call__(self, *args, **kwargs):
        print("__call__ is running...")

    def __del__(self):
        print("__del__ is running...")


MyClass()  # 匿名对象程序并未使用到,执行完后就销毁了
print("----------------------")

a = MyClass()  # 这里会先执行__new__ 在执行 __init__
assert hasattr(a, "__del__")  # True
print(callable(a))  # True  可以被调用时结果为True,对象如果没有__call__ 属性则是False
assert hasattr(lambda x, y: x + y, "__call__")  # True
print(callable(lambda x, y: x + y))  # True
```



### 4.2 `__str__` 和 `__repr__`

> 两个方法都只是为了自定义对象的打印信息  
>
> 对象被打印时执行,一般默认先找str, str没有则使用repr

```Python
class A(object):

    def __init__(self):
        self.name = "李四"

    def __str__(self):
        print("__str__ is running ...")
        return "str"

    def __repr__(self):
        print("__repr__ is running ...")
        return ""


print(A())  # 默认为 <__main__.A object at 0x1043aa710>
```



### 4.3 compare系列

```python
class Student:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        print("__eq__ is running ... 可自定义比较逻辑")
        if isinstance(other, Student):
            return self.age == other.age  # 返回布尔值
        return False


print(Student(18) == Student(18))
print(Student(18) != 18)  # nq, 不相等的逻辑。如果没有实现，则默认是eq的结果取反。
print(dir(Student(18)))  # __lt__、__gt__、__le__、__ge__ 分别表示小于、大于、小于等于和大于等于。
```



### 4.4 attr系列

```Python
class MyClass(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        print("getattr 获取不存在的对象属性时触发")
        # super().__delattr__(item)  # 'MyClass' object has no attribute 'id'
        return self.__dict__.get(item)

    def __setattr__(self, key, value):
        print("setattr 设置修改对象属性时触发")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print("delattr 删除对象属性时触发")
        if item == "name":  # 属性是name时抛出异常，或者不进行删除操作
            # raise AttributeError("name 属性不让删除...")
            pass
        else:
            super().__delattr__(item)

    def __getattribute__(self, name):
        # 访问任何属性（包括存在的和不存在的属性）时都会调用 __getattribute__ 方法
        print("__getattribute__ called")
        return super().__getattribute__(name)


a = MyClass("李四", 18)  # 每一次给属性赋值 都会执行setattr方法
print(a.id)
del a.age  # 触发delattr方法
print(f"查看对象属性:{a.__dict__}")
```



### 4.5 item系列

```python
# 一个普通对象通过[] 操作取值时会触发 __getitem__
class Person(object):

    def __setitem__(self, key, value):
        print("setitem []设置值时触发")
        setattr(self, key, value)

    def __getitem__(self, item):
        print("getitem []取值时触发")
        return getattr(self, item)

    def __delitem__(self, key):
        print("delitem del p[key]时触发", key)


p = Person()
p['id'] = 1  # 触发setitem方法
print(p['id'])  # 触发getitem方法
del p['id']  # 触发delitem方法
```



### 4.6 `__enter__` 和 `__exit__`

> 上下文管理器: 支持"上下文管理协议"的对象,包含 __enter__() 和 __exit__() 方法
> with 可以操作一个 支持上下文管理协议的对象

```python
class MyOpen:
    def __init__(self, file_name: str, mode="r"):
        self.file = open(file_name, mode)

    def __enter__(self):
        print("进入with语句块时触发")
        return self.file  # 返回值赋值给 as后面的接收值

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出with语句块时触发,不论with语句块是否有异常报错，__exit__都会被执行")
        self.file.close()


with MyOpen("test", "w") as f:
    f.write("hello world")
```



### 4.7 `__slots__` 

> 该类实例只能创建__slots__中声明的属性，否则报错, 具体作用就是节省内存

```python
from memory_profiler import profile


class Test(object):
    __slots__ = ['a', 'name']

    def __init__(self, name):
        self.name = name


Test.c = 3  # 类属性仍然可以自由添加
t = Test("xx")
t.a = 1
print(t.c)  # 绕过限制就是给类添加属性
# t.b = 2  # AttributeError: 'Test' object has no attribute 'b'


class TestA(object):
    __slots__ = ['a', 'b', 'c']

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class TestB(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


@profile
def func_02():
    temp = [TestA(i, i + 1, i + 2) for i in range(10000)]
    del temp
    temp = [TestB(i, i + 1, i + 2) for i in range(10000)]
    del temp


func_02()
```



### 4.8 `__add__`、 `__dict__`、 `__bases__`、 `__all__`

> `__add__`:  手动实现相加操作
> `__dict__`: 获取对象的属性
> `__bases__`: 获取类继承的元素
> `__all__`: 当其它文件以“from 模块名 import *”的形式导入该模块时，该文件中只能使用 `__all__` 列表中指定的成员

```python
class MyClass(object):

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # other这里传入的是第二个对象 obj2  obj2.value ==》 __init__ 初始化中传入的value
        return self.value + other.value


a = MyClass(10)
print(a + MyClass(20))
print(MyClass.__dict__)


# __bases__  这是一个元祖，里面的元素是继承的类
class A(object):
    pass


print(A.__bases__)

# 当其它文件以“from 模块名 import *”的形式导入该模块时，该文件中只能使用 `__all__` 列表中指定的成员
__all__ = ["MyClass"]
```

