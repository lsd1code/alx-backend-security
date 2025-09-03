from django.db import models


class RequestLog(models.Model):
    ip_address = models.CharField(max_length=32, null=False)
    path = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.ip_address}'  # type:ignore


class BlockedIP(models.Model):
    ip_address = models.CharField(max_length=32, null=False, unique=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.ip_address}'  # type:ignore
