# netbox_plugin_auvik/navigation.py

from extras.plugins import PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_plugin_auvik:device_status',
        link_text='Auvik Device Status',
        permissions=['netbox_plugin_auvik.view_auvikdevicestatus'],
        buttons=(
            PluginMenuItem(
                link='plugins:netbox_plugin_auvik:device_status',
                title='View Auvik Device Status',
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
)
