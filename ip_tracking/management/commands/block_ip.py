from typing import Any
from django.core.management.base import BaseCommand

from ip_tracking.models import BlockedIP


class Command(BaseCommand):
    help = "Adds a blocked IP address to the system."
    ip_addresses = [
        {"ip_address": "127.0.0.3"},
        {"ip_address": "127.0.0.4"},
        {"ip_address": "127.0.0.5"},
    ]

    def handle(self, *args: Any, **options: Any) -> str | None:
        for object in self.ip_addresses:
            BlockedIP.objects.create(ip_address=object['ip_address'])

        self.stdout.write(
            self.style.SUCCESS("✅ Success ✅")
        )
