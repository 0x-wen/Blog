# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 16:32
# @Author  :  Jw
# @File    : operate_yaml.py
import yaml

from tools.constants import YAML_DATA_PATH


class OperateYaml:

    def read_yaml(self):
        """读取yaml文件"""
        with open(YAML_DATA_PATH, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def get_value(self, key, port):
        """获取数据"""
        data = self.read_yaml()
        value = data[key][port]
        return value

    def write_data(self, i, device, bp, port):
        """写入数据"""
        data = self.join_data(i, device, bp, port)
        with open(YAML_DATA_PATH, "a") as fr:
            yaml.dump(data, fr)

    def join_data(self, i, device, bp, port):
        """拼接写入数据"""
        data = {
            "user_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def clear_data(self):
        """清除数据"""
        with open(YAML_DATA_PATH, "w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        data = self.read_yaml()
        return len(data)


if __name__ == '__main__':
    print(YAML_DATA_PATH)
    a = OperateYaml()
    print(a.get_value("user_info_0", "port"))

