# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 16:14
# @Author  :  Jw
# @File    : server.py
import multiprocessing
import threading
import time

from tools.base_page import ExecuteTermination
from tools.operate_log import do_log
from tools.operate_yaml import OperateYaml


class Port:

    def port_is_used(self, port_num, environment="mac"):
        """
        判断端口是否被占用
        environment: 运行环境 默认为mac
        """
        flag = None
        mac_command = "netstat -anp tcp | grep " + str(port_num)
        win_command = 'netstat -ano | findstr ' + str(port_num)
        if environment == "win":
            result = ExecuteTermination.execute_result(win_command)
        else:
            result = ExecuteTermination.execute_result(mac_command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def port_list(self, start_port, devices_list, environment="mac"):
        """
        生成未被占用的端口
        start_port: 开始端口
        devices_list: 设备信息
        environment: 为win运行环境时 查找端口是否被占用方式不一样
        """
        port_list = []
        if devices_list is not None:
            while len(port_list) != len(devices_list):
                if not self.port_is_used(start_port, environment=environment):
                    port_list.append(start_port)
                start_port += 1
            return port_list
        else:
            do_log.info("生成可用端口失败，请检查传入参数信息 start_port:{}, devices_list:{}".format(start_port, devices_list))
            return None


class Server:

    def __init__(self):
        self.device_list = self.get_devices()
        self.operate_yaml_obj = OperateYaml()

    def get_devices(self, environment="mac"):
        """
        获取设备信息
        environment: 运行环境 默认为mac
        """
        devices_list = []
        result = ExecuteTermination.execute_result(command="adb devices")

        if len(result) >= 2:  # 至少要有一个设备信息
            if environment == "win":
                for i in result:
                    if 'List' in i:
                        continue
                    devices_info = i.split('\t')
                    if devices_info[1] == 'device':
                        devices_list.append(devices_info[0])
            else:
                for j in result:
                    for k in j:
                        if k == "":
                            continue
                        elif "List" in k:
                            continue
                        devices_info = k.split('\t')
                        if devices_info[1] == "device":
                            devices_list.append(devices_info[0])
            do_log.info("已找到设备信息:{}".format(devices_list))
            return devices_list
        else:
            do_log.info("没找到设备信息，请检查连接设备.")
            return None

    def create_port_list(self, start_port, environment="mac"):
        """
        根据当前设备创建可用端口
        environment: 创建可用端口时，这里注意传入平台信息
        :return 可用端口信息
        """
        port = Port()
        port_list = port.port_list(start_port=start_port, devices_list=self.device_list, environment=environment)
        return port_list

    def create_command_list(self, i):
        """生成启动命令"""
        command_list = []
        appium_port_list = self.create_port_list(start_port=4700)
        bootstrap_port_list = self.create_port_list(start_port=4900)
        device_list = self.get_devices()

        command = "appium -p {} -bp {} -U {}".format(str(appium_port_list[i]), str(bootstrap_port_list[i]),
                                                     device_list[i])
        command_list.append(command)
        self.operate_yaml_obj.write_data(i, device_list[i], str(bootstrap_port_list[i]),
                                         str(appium_port_list[i]))

        return command_list

    def start_server(self, i):
        """启动服务"""
        start_list = self.create_command_list(i)
        print("第{}个线程信息：{}".format(i, start_list))

        ExecuteTermination.execute(command=start_list[0])

    def kill_server(self):
        """关闭服务 - mac下命令"""
        ExecuteTermination.execute(command="kill -s 9 `pgrep node`")
        pass

    def main(self):
        thread_list = []
        self.kill_server()
        self.operate_yaml_obj.clear_data()

        for i in range(len(self.device_list)):
            appium_start = multiprocessing.Process(target=self.start_server, args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            j.start()
        time.sleep(20)


if __name__ == '__main__':
    # print(Server.get_devices())
    # print(Port().create_port_list(start_port=4720, devices_list=[1, 2, 2, 1]))
    server = Server()
    server.main()

    pass
