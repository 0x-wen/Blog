from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from configures.models import Configures
from debugtalks.models import DebugTalks
from envs.models import Envs
from interfaces.models import Interfaces
from projects.models import Projects
from reports.models import Reports
from testcases.models import TestCases
from testsuits.models import TestSuits


class SummaryView(APIView):
    permission_class = [permissions.IsAuthenticated]  # 设置这个视图类,只有登录了才有权限查看

    def get(self, request, *args, **kwargs):
        user = request.user
        user: User

        if date_joined := user.date_joined:
            date_joined = date_joined.strftime('%Y-%m-%d %H:%M:%S')
        else:
            date_joined = ''

        if last_login := user.last_login:
            last_login = last_login.strftime('%Y-%m-%d%H:%M:%S')
        else:
            last_login = ''

        executed_testcases_count = Reports.objects.aggregate(testcases=Sum('count'))['testcases']
        pass_testcases_count = Reports.objects.aggregate(success=Sum('success'))['success']
        success_rate = int(pass_testcases_count / executed_testcases_count * 100)
        fail_rete = 100 - success_rate
        data = {
            'user': {
                "username": user.username,
                "role": '管理员' if user.is_superuser else '普通用户',
                "date_joined": date_joined,
                "last_login": last_login,
            },
            'statistics': {
                "projects_count": Projects.objects.count(),
                "interfaces_count": Interfaces.objects.count(),
                "testcases_count": TestCases.objects.count(),
                "testsuits_count": TestSuits.objects.count(),
                "configures_count": Configures.objects.count(),
                "envs_count": Envs.objects.count(),
                "debug_talks_count": DebugTalks.objects.count(),
                "reports_count": Reports.objects.count(),
                "success_rate": success_rate,
                "fail_rete": fail_rete,
            }
        }
        return Response(data, status=200)
