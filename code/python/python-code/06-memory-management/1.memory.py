# 1.python与c语言中的内存管理
"""
C语言中内存分配方法有2种
第一种：int a = 1; char s[10] = "hello"; 在栈区申请内存  栈内存的特点: 出了栈作用域自动销毁
第二种：malloc()在堆区申请内存, free() 释放内存

Python语言中：所有的对象都是在堆区申请内存    # 堆内存必须手动销毁，python解释器做垃圾回收 自动销毁
对象没有被使用了 就释放内存，怎么知道对象没有被使用了呢？
引用计数： 引用次数会从大到小, 在cpython源码中 有一个结构体，中有一个参数类标识 引用计数
垃圾回收： 当引用计数为0时，回收对象所占的内存.python解释器负责
"""

import sys

print(sys.getsizeof(8))  # 28字节 C语言中int 是4个字节

"""
python 没有C语言省内存的原因：
python 存储一个int类型的数据：需要引用次数, 类型, 值  内存换来了语言的易用性
C语言  存储一个int类型的数据：只需要值（不需要引用次数,类型已经在写代码时申明）
"""

"""
# 引用计数：sys.getrefcount(obj) 可以查看obj被引用了多少次
# 调用getrefcount函数时，引用+1
导致+1的情况：
- 赋值，引用   obj = 1,  obj=MyClass()
- 被其他对象使用  one_list.append(obj)
- 对象作为参数传递给函数  func(obj)
导致-1的情况：
- 改变引用对象(重新引用其他对象)
- 销毁 del x
- 函数调用结束
"""


class MyClass(object):
    pass


def f(obj):
    print(f"函数调用之后，引用次数为：{sys.getrefcount(obj)}")
    pass


def main():
    obj = MyClass()
    x = obj
    print(sys.getrefcount(obj))
    f(obj)  # 函数调用结束，引用次数会减少
    print(sys.getrefcount(obj))


if __name__ == '__main__':
    main()
