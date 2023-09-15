# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 15:23
# @Author  : Jw
# @File    : crontab_build.py
from crontab import CronTab


class CrontabUpdate(object):

    def __init__(self):
        # 创建当前用户的crontab，当然也可以创建其他用户的，但得有足够权限
        self.cron = CronTab(user=True)

    def add_crontab_job(self, command_line, time_str, comment_name):
        # 创建任务
        job = self.cron.new(command=command_line)
        # 设置任务执行周期
        job.setall(time_str)
        # 给任务添加一个标识，给任务设置comment，这样就可以根据comment查询
        job.set_comment(comment_name)
        # 将crontab写入配置文件
        self.cron.write_to_user()  # 指定用户，写入指定用户下的crontab任务

    def del_crontab_jobs(self, comment_name):
        # 根据comment查询，当时返回值是一个生成器对象，
        # 不能直接根据返回值判断任务是否存在，
        # 如果只是判断任务是否存在，可直接遍历my_user_cron.crons
        # 返回所有的定时任务，返回的是一个列表
        # 按comment清除定时任务
        # self.cron.remove_all(comment=comment_name)
        # 按comment清除多个定时任务，一次write即可
        self.cron.remove_all(comment=comment_name)
        self.cron.remove_all(comment=comment_name + ' =')
        self.cron.write_to_user()  # 指定用户,删除指定用户下的crontab任务

    def del_all_crontab_jobs(self):
        # 指定用户,删除指定用户下所有的crontab任务
        self.cron.remove_all()
        self.cron.write_to_user()


def get_period(period):
    ret = None
    if period == '5min':
        ret = '*/5 * * * *'
    elif period == 'hour':
        ret = '0 * * * *'
    elif period == 'day':
        ret = '0 8 * * *'

    return ret


# def update_crontab(clu_nid, add_nid, period, del_nid):
#     command_line = EXEC_ENV + EXEC_FILE + clu_nid
#
#     # 创建一个实例
#     crontab_update = CrontabUpdate()
#     # 调用函数新增一个crontab任务
#     try:
#         if del_nid == '*':
#             crontab_update.del_all_crontab_jobs()
#         elif del_nid:
#             crontab_update.del_crontab_jobs(del_nid)
#         if add_nid:
#             period_time = get_period(period)
#             if not period_time:
#                 return None
#             crontab_update.add_crontab_job(command_line, period_time, add_nid)
#
#     except Exception as err:
#         logger.error(err)
