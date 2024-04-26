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
    return cpu_load, memory_usage

def dashboard_callback(request, context):

    cpu_load, memory_usage = get_server_load()

    context.update(
        {
            "performance": [
                {
                    "title": _("Server Load"),
                    "chart": json.dumps({
                        "labels": ["CPU Load", "Memory Usage"],
                        "datasets": [{
                            "label": "Server Metrics",
                            "data": [cpu_load, memory_usage],
                            "backgroundColor": ["#ff6384", "#36a2eb"],
                            "borderColor": ["#ff6384", "#36a2eb"],
                        }]
                    }),
                    "footer": mark_safe("<strong class='text-red-600 font-medium'>Real-time data</strong>&nbsp;updated every minute")
                },
            ],
        }
    )

    return context
