# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 23:31
# @Author  : Jw
# @File    : common.py
import json
import os
from datetime import datetime

import yaml
from httprunner.task import HttpRunner
from rest_framework.response import Response

from configures.models import Configures
from debugtalks.models import DebugTalks
from envs.models import Envs
from reports.models import Reports
from testcases.models import TestCases


def generate_testcase_file(instance: TestCases, env: Envs, suites_dir):
    """
    创建运行工程目录结构
    @param instance: TestCases 模型对象
    @param env: Envs 模型对象
    @param suites_dir: 以时间戳命名的项目目录
    @return:
    """
    # 获取当前用例所属项目名称、所属接口名称
    interface_name = instance.interface.name
    project_name = instance.interface.project.name

    # 构建以所属项目名称的路径
    testcase_dir_path = os.path.join(suites_dir, project_name)
    if not os.path.exists(testcase_dir_path):
        os.makedirs(testcase_dir_path)
        # 1.创建debugtalk.py
        debugtalk_obj = DebugTalks.objects.filter(project__name=project_name).first()
        debugtalk_obj: DebugTalks
        with open(os.path.join(suites_dir, 'debugtalk.py'), 'w', encoding='utf-8') as file:
            file.write(debugtalk_obj.debugtalk)

    # 2.创建以接口命名的路径
    testcase_dir_path = os.path.join(testcase_dir_path, interface_name)
    if not os.path.exists(testcase_dir_path):
        os.makedirs(testcase_dir_path)

    # 3.创建yaml配置文件
    testcase_list = list()
    setup_data = json.loads(instance.setup)
    config_id = setup_data.get('config')
    base_url = env.base_url if env.base_url else ''
    if config_id is not None:
        config_obj = Configures.objects.filter(pk=config_id).first()
        config_obj: Configures
        config_data = json.loads(config_obj.request)
        config_data['config']['request']['base_url'] = base_url
    else:
        config_data = {
            "config": instance.name,
            "request": {
                "base_url": base_url
            }
        }
    testcase_list.append(config_data)

    # 4.获取前置用例信息
    testcases_id = setup_data.get("testcases")
    if testcases_id:
        for case_id in testcases_id:
            setup_testcase_obj = TestCases.objects.filter(pk=case_id).first()
            try:
                setup_testcase_request = json.loads(setup_testcase_obj.request)
            except Exception as e:
                print(f'前置用例数据转换出错{e}')
                continue
            testcase_list.append(setup_testcase_request)

    # 4.获取当前用例信息
    try:
        current_testcase_request = json.loads(instance.request)
        testcase_list.append(current_testcase_request)
    except Exception as e:
        print(f'当前用例数据转换出错{e}')
        raise e

    # 5.将当前testcase_list中的数据转换为yaml配置文件
    testcase_dir_path = os.path.join(testcase_dir_path, instance.name + '.yaml')
    with open(testcase_dir_path, 'w', encoding='utf-8') as file:
        yaml.dump(testcase_list, file, allow_unicode=True)
    pass


def create_report(runner: HttpRunner, instance: TestCases):
    report_name = instance.name
    time_stamp = int(runner.summary['time']['start_at'])
    start_datetime = datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    runner.summary['time']['start_datetime'] = start_datetime
    # duration保留3位小数
    runner.summary['time']['duration'] = round(runner.summary['time']['duration'], 3)
    runner.summary['html_report_name'] = report_name

    for item in runner.summary['details']:
        try:
            for record in item['records']:
                record['meta_data']['response']['content'] = record['meta_data']['response']['content'].decode('utf-8')
                record['meta_data']['response']['cookies'] = dict(record['meta_data']['response']['cookies'])

                request_body = record['meta_data']['request']['body']
                if isinstance(request_body, bytes):
                    record['meta_data']['request']['body'] = request_body.decode('utf-8')
        except Exception as e:
            print(f'转换成功runner.summary数据错误:{e}')
            raise e

    summary = json.dumps(runner.summary, ensure_ascii=False)
    report_name = report_name + '_' + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    report_path = runner.gen_html_report(report_name)

    with open(report_path, encoding='utf-8')as stream:
        reports = stream.read()

    test_report = dict(name=report_name, result=runner.summary.get('success'),
                       success=runner.summary.get('stat').get('successes'),
                       count=runner.summary.get('stat').get('testsRun'),
                       html=reports, summary=summary)
    report_obj = Reports.objects.create(**test_report)

    return report_obj.id


def run_testcase(instance, suites_dir):
    runner = HttpRunner()
    try:
        runner.run(suites_dir)
    except Exception as e:
        print(f'用例执行失败{e}')
        return Response({'msg': "用例执行失败"}, status=400)

    # 创建报告
    report_id = create_report(runner, instance)

    return Response({'id': report_id}, status=201)
