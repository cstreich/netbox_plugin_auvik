import requests
from django.conf import settings
from .models import AuvikDeviceStatus
from dcim.models import Device

def fetch_auvik_device_status(device_id):
    device = Device.objects.get(id=device_id)
    api_url = f"https://auvikapi.us1.my.auvik.com/v1/devices/{device_id}"
    api_key = settings.AUVIK_API_KEY

    response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})

    if response.status_code == 200:
        data = response.json()
        status = data.get("status", "unknown")

        # Update or create the AuvikDeviceStatus entry
        AuvikDeviceStatus.objects.update_or_create(
            device=device,
            defaults={"status": status}
        )
    else:
        raise Exception(f"Failed to fetch Auvik status: {response.content}")
