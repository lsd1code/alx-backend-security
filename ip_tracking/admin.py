from django.contrib import admin

from ip_tracking.models import BlockedIP, RequestLog

admin.site.register(BlockedIP)
admin.site.register(RequestLog)
