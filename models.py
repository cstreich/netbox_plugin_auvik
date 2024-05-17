from django.db import models
from netbox.models import NetBoxModel

class AuvikDeviceStatus(NetBoxModel):
    device = models.OneToOneField(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name='auvik_status'
    )
    status = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device.name}: {self.status}"
