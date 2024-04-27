import json
import random
import psutil

from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView

class HomeView(RedirectView):
    pattern_name = "admin:index"

def get_server_load():
    cpu_load = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    ramTotal = psutil.virtual_memory()[0] / 1024000000
    ramUsed = psutil.virtual_memory()[3] / 1024000000
    ramUsedInPercent = psutil.virtual_memory()[2]
    diskUsed = psutil.disk_usage('/')[3]
    return cpu_load, memory_usage, ramTotal, ramUsed, ramUsedInPercent, diskUsed

def dashboard_callback(request, context):

    performance_negative2 = [[-1, -random.randrange(1, 28)] for i in range(1, 8)]
    performance_negative3 = [[-1, -random.randrange(8, 28)] for i in range(1, 8)]
    cpu_load, memory_usage, ramTotal, ramUsed, ramUsedInPercent, diskUsed = get_server_load()
    context.update(
        {
            "kpi": [
                {
                    "title": "memory usage",
                    "metric": f"{memory_usage}mb",
                },
                {
                        "title": "CPU load",
                    "metric": f"{cpu_load}ed",
                },
                {
                    "title": "Disc load",
                    "metric": f'Ram used: {ramUsed} GB ({ramUsedInPercent}%) Disk used: {diskUsed}% ',
                },
            ],
            "performance": [
                {
                    "title": _("CPU Load"),
                    "chart": json.dumps({
                        "labels": ["16:00", "16:01","16:02","16:03","16:04","16:05","16:06"],
                        "datasets": [
                            {"data": performance_negative2, "borderColor": "#f43f5e"}
                        ],
                    }),
                    "footer": mark_safe("<strong class='text-red-600 font-medium'>Real-time data</strong>&nbsp;updated every minute")
                },
                {
                "title": _("RAM usage"),
                "footer": mark_safe(
                    '<strong class="text-green-600 font-medium">+3.14%</strong>&nbsp;progress from last week'
                ),
                "chart": json.dumps(
                    {
                        "labels": ["16:00", "16:01","16:02","16:03","16:04","16:05","16:06"],
                        "datasets": [
                            {"data": performance_negative3, "borderColor": "#f43f5e"}
                        ],
                    }
                ),
                },
            ],
        }
    )

    return context
