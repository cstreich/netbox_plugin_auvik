from setuptools import find_packages, setup

setup(
    name='netbox_plugin_auvik',
    version='0.1',
    description='A NetBox plugin to display Auvik device status',
    url='https://your-repo-url/netbox_plugin_auvik',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',  # Add any other dependencies here
    ],
    include_package_data=True,
    zip_safe=False,
)
