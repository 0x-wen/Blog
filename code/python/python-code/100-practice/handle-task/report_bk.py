# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 13:23
# @Author  : Jw
# @File    : report_bk.py
import os

import paramiko


class SSHConnection(object):

    def __init__(self, host_info):
        self.host = host_info['host']
        self.port = host_info['port']
        self.username = host_info['username']
        self.pwd = host_info['pwd']
        self.__transport = self.connect()
        self.sftp = paramiko.SFTPClient.from_transport(self.__transport)

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        return transport

    def close(self):
        self.__transport.close()

    def run_cmd(self, command):
        """
         执行shell命令,返回字典
         return {'color': 'red','res':error}或
         return {'color': 'green', 'res':res}
        :param command:
        :return:
        """
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        res = to_str(stdout.read())
        # 获取错误信息
        error = to_str(stderr.read())
        # 如果有错误信息，返回error
        # 否则返回res
        if error.strip():
            return {'color': 'red', 'res': error}
        else:
            return {'color': 'green', 'res': res}

    def upload(self, local_path, target_path):
        """上传文件"""
        # 将location.py 上传至服务器 /tmp/test.py
        self.sftp.put(local_path, target_path, confirm=True)
        # print(os.stat(local_path).st_mode)
        # 增加权限
        # sftp.chmod(target_path, os.stat(local_path).st_mode)
        self.sftp.chmod(target_path, 0o755)  # 注意这里的权限是八进制的，八进制需要使用0o作为前缀

    def download(self, target_path, local_path):
        """下载文件"""
        # 将location.py 下载至服务器 /tmp/test.py
        self.sftp.get(target_path, local_path)

    def download_dir(self, target_path, local_path):
        """复制远程目录到本地"""
        try:
            check_local_dir(local_path)  # 创建本地目录
            remote_files = self.sftp.listdir(target_path)
            for file in remote_files:  # 遍历读取远程目录里的所有文件
                # 删除服务器中测试报告名称 为后缀.xml文件
                if file.endswith('_output.xml'):
                    self.sftp.remove(target_path + file)
                local_file = local_path + file
                remote_file = target_path + file
                self.download(target_path=remote_file, local_path=local_file)
        except IOError:  # 如果目录不存在则抛出异常
            return "remote_path or local_path is not exist"
        self.__del__()

    # 销毁
    def __del__(self):
        self.__transport.close()


def check_local_dir(local_path):
    """检查本地目录是否存在，不存在就创建"""
    if not os.path.exists(local_path):
        os.makedirs(local_path)


def to_str(bytes_or_str):
    """
    把byte类型转换为str
    :param bytes_or_str:
    :return:
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def cp_dir():
    host_dict = dict(host='XXX', port=22, username='XXX', pwd='XXX')
    one_obj = SSHConnection(host_info=host_dict)

    one_obj.download_dir(target_path='/root/bff-interface_autotest/report/',
                         local_path='/Users/jw/Downloads/test/')


if __name__ == '__main__':
    cp_dir()
