# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 17:23
# @Author  : Jw
# @File    : 4.python中finally.py


def test_finally():
    var1 = 0
    print(f"init_id:{id(var1)}")
    var2 = [1]
    try:
        var1 += 5000
        print(f'try is run... id:{id(var1)}')
        tmp1, tmp2 = var1, var2  # var1 值传递 到finally中
        print(f'tmp1 id:{id(tmp1)}')  # return tmp1
        assert id(tmp1) == id(var1)  # 验证tmp1和var1 是同一个地址
        return tmp1, tmp2
    except Exception as e:
        pass
    finally:
        print(f'finally var1 id:{id(var1)}, value:{var1}')  # 此时内存地址 和 var1一样
        var1 += 5
        print(f'finally var1 id:{id(var1)}, value:{var1}')  # var1是值传递，复制一份在做加法，所以ID会更改
        var2.append(2)
        var2.append(3)
        print('finally is run...')


if __name__ == '__main__':
    print(test_finally())

    pass
