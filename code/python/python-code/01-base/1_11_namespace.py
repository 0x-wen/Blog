# -*- coding: utf-8 -*-
"""
闭包
1.在一个函数内部定义了另一个函数
2.内部函数引用了外部函数的变量
"""
# 一般有三种命名空间：
# 内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
# 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

# Python的作用域一共有4种，分别是：
# L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
# E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。
# 比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
# G（Global）：当前脚本的最外层，比如当前模块的全局变量。
# B（Built-in）： 包含了内建的变量/关键字等。，最后被搜索
# 规则顺序： L –> E –> G –> gt; B

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
