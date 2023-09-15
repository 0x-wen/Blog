# -*- coding: utf-8 -*-

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
