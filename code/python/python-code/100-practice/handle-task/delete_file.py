# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 16:10
# @Author  : Jw
# @File    : delete_file.py
from pathlib import Path


def remove_file(path, pattern: str):
    """删除文件"""
    for file in Path(path).glob(pattern):
        file.unlink(file)
    return f'已删除指定pattern:{pattern}文件'


def main():
    print(remove_file(path='/Users/jw/Downloads/test/', pattern='*_output.xml'))
    pass


if __name__ == '__main__':
    main()
