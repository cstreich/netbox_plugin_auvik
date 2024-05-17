# NetBox Plugin Auvik

This is a NetBox plugin that integrates with the Auvik API to display the status of devices on their respective device pages in NetBox.

## Features

- Fetch device status from Auvik API
- Display device status on the NetBox device page

## Installation

1. Clone the repository and navigate to the plugin directory:

    ```bash
    git clone https://your-repo-url/netbox_plugin_auvik.git
    cd netbox_plugin_auvik
    ```

2. Install the plugin using pip:

    ```bash
    pip install .
    ```

3. Add the plugin to your NetBox configuration (`configuration.py`):

    ```python
    PLUGINS = [
        'netbox_plugin_auvik',
    ]

    PLUGINS_CONFIG = {
        'netbox_plugin_auvik': {
            'AUVIK_API_KEY': 'your_auvik_api_key_here',
        }
    }
    ```

4. Run migrations to set up the database tables:

    ```bash
    python3 manage.py makemigrations netbox_plugin_auvik
    python3 manage.py migrate netbox_plugin_auvik
    ```

## Usage

After installation, you will see a new menu item for "Auvik Device Status" in the NetBox interface. Navigate to a device page to view the status fetched from the Auvik API.

## Configuration

Make sure to set your Auvik API key in the NetBox configuration file:

```python
PLUGINS_CONFIG = {
    'netbox_plugin_auvik': {
        'AUVIK_API_KEY': 'your_auvik_api_key_here',
    }
}
