# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/15 15:14
# @Author  : JW
# @FileName: handle_upload_file.py
"""
import win32gui
import win32con


def upload_file(file_path):
    """上传文件封装"""
    # 一级窗口
    dialog = win32gui.FindWindow("#32770", "打开")
    # 二级窗口
    comboxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    # 三级窗口
    combox = win32gui.FindWindowEx(comboxEx32, 0, "ComboBox", None)
    # Edit元素
    edit = win32gui.FindWindowEx(combox, 0, "Edit", None)

    # 打开按钮元素
    button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")

    # 输入文件完整路径
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
    # 点击打开按钮提交
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


if __name__ == '__main__':
    file_path = r"F:\jkb_sandbox_palt_web\logs\test_img\photo.png"
    upload_file(file_path)
