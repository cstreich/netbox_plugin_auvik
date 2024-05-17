from extras.plugins import PluginConfig

class NetBoxPluginAuvikConfig(PluginConfig):
    name = 'netbox_plugin_auvik'
    verbose_name = 'NetBox Plugin Auvik'
    description = 'A NetBox plugin to display Auvik device status'
    version = '0.1'
    author = 'Your Name'
    author_email = 'your.email@example.com'
    base_url = 'auvik'
    required_settings = []
    default_settings = {
        'AUVIK_API_KEY': '',
    }

config = NetBoxPluginAuvikConfig
