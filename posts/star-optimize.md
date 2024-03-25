---
layout: post
title: "项目优化篇"
date: 2023-08-21  
tags: [python]
---

### [**back**](../index.html)


## 1.解决api请求变更,URL和参数更新维护等问题？

引入客户端代码生成工具,根据接口文档自动生成代码,从而减少由于接口变更的维护成本

官网地址: https://swagger.io/tools/swagger-codegen/

- 下载swagger codegen 
- 生成对应语言客户端代码  [-i 指定api接口路径,-lang 指定语言,-o 指定生成代码文件路径]

**阅读生成项目的readme,提供了使用教程**​		
```python
swagger-codegen generate -i http://ip:port/static/openapi.yml --lang python -o ./me_api_client
swagger-codegen generate -i http://ip:port/static/openapi.yml --lang go -o ./me_api_client
```




## 2. 项目结构分析

1. 客户端需要连接到指定节点，能提供多节点测试
2. 客户端需要提供命令生成器 和 执行器
3. 操作每个模块都需要自定义其模块方法，成本较高，并且大致逻辑一致



Node模块：

- 初始化node实例提供连接节点功能
- node实例默认提供对应 交易的一些常用命令设置
- node都绑定有执行器(executor) 和 命令生成器（generate_xxx）

```python
import inspect
from typing import Callable

from loguru import logger

from config.config import app_chain
from ssh import Client, Result


class Node:
    ssh_client = Client(ip=app_chain.Host.ip, port=app_chain.Host.port,
                        username=app_chain.Host.username, password=app_chain.Host.password)
    config = app_chain

    def __init__(self, node: str):
        super().__init__()
        if "--node" not in node:
            node = f"--node={node}"
        self.config.Flags.node = node
        self.superadmin = self.__get_superadmin_addr()
        self.__init_instance_config()

    def update_config(self, attr: str, key: str, value: str):
        """
        If key exists in the attr object, replace the value. If no, add the value
        :param attr: 'ApplicationChain' object must have attr
        :param key:
        :param value:
        :return:
        """
        sub_cfg_gen = getattr(self.config, attr)
        found_key = False
        for i in sub_cfg_gen:
            if i[0] == key:
                setattr(sub_cfg_gen, key, value)
                found_key = True
                break
        if not found_key:
            setattr(sub_cfg_gen, key, value)

    def __init_instance_config(self):
        self.update_config("Flags", "fees", "--fees=100umec")
        self.update_config("Flags", "gas", "--gas=200000")

    @property
    def base_cmd(self):
        return f"{self.config.Host.chain_work_path} "

    def __get_superadmin_addr(self):
        get_superadmin_cmd = f"{self.base_cmd} keys show superadmin -a {self.config.Flags.keyring_backend}"
        return self.ssh_client.exec_cmd(get_superadmin_cmd)

    def generate_query_cmd(self, cmd: str):
        query_cmd = self.base_cmd + f"{self.config.Flags.node} {self.config.GlobalFlags.chain_id} "
        return query_cmd + cmd

    def generate_tx_cmd(self, cmd: str):
        tx_cmd = self.base_cmd + (f"{self.config.Flags.fees} {self.config.Flags.gas} "
                                  f"{self.config.Flags.yes} {self.config.Flags.keyring_backend} "
                                  f"{self.config.Flags.node} {self.config.GlobalFlags.chain_id} ")
        return tx_cmd + cmd

    def generate_keys_cmd(self, cmd: str):
        keys_cmd = self.base_cmd + f"{self.config.Flags.keyring_backend} "
        return keys_cmd + cmd

    def executor(self, cmd):
        logger.info(f"{inspect.stack()[0][3]}: {cmd}")
        if "keys add" in cmd:
            _ = self.ssh_client.channel.send(cmd + "\n")
            resp_info = self.ssh_client.Interactive.read_channel_data(self.ssh_client.channel)
            if "existing" in resp_info:
                resp_info = self.ssh_client.Interactive.input_yes_or_no(self.ssh_client.channel)
            assert "**Important**" in resp_info
            return resp_info

        resp_info = self.ssh_client.exec_cmd(cmd, strip=False)
        if resp_info.failed:
            logger.info(f"resp_info.stderr: {resp_info.stderr}")
            return resp_info.stderr
        return Result.yaml_to_dict(resp_info.stdout)
```



Meta元类:

为每个类动态生成方法,解决其定义冗余

```python
class Meta(type):
    def __init__(cls, name, bases, attrs):
        cls.module = name.lower()  # 创建类module = 其类名称小写
        super().__init__(name, bases, attrs)

        sub_module = attrs.get('sub_module', [])
        parent_module = attrs.get('parent_module', '')
        if isinstance(sub_module, list):
            for module in sub_module:
              	# 添加类方法，名称为其子模块
                method = cls.generate_method(parent_module, module)
                setattr(cls, module, classmethod(method))
        elif isinstance(sub_module, dict):
            for k, module in sub_module.items():
                method = cls.generate_method(parent_module, module)
                setattr(cls, k, classmethod(method))
        else:
            raise f"sub_module type error: {type(sub_module)}, expect list or dict"

    @staticmethod
    def generate_method(parent_module, sub_module) -> Callable[..., str]:
       # 利用闭包特性，生成的类方法只接受 *args,**kwargs 参数
        def method(cls, *args, **kwargs):
            return cls.build_command(parent_module, sub_module, *args, **kwargs)

        return method

    def build_command(cls, parent_module, sub_module, *args, **kwargs):
        args_str = " ".join(map(str, args))
        kwargs_str = " ".join([f"--{key}={value}" for key, value in kwargs.items() if value != ""])
        return f"{parent_module} {cls.module} {sub_module} {args_str} {kwargs_str} "

    def __getattr__(cls, attr):
        raise AttributeError(f"'{cls.__name__}' class has no attribute '{attr}'")

    def help(cls):
        for attr_name in cls.sub_module:
            attr = getattr(cls, attr_name)
            if not callable(attr):
                raise TypeError(f"attribute '{attr_name}' is not callable")
        print(f"Available methods: {list(cls.sub_module)}")
        print(f"Example usage: {cls.__name__}.{list(cls.sub_module)[0]}('argument')")
```



