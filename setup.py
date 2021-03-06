from setuptools import find_packages
from setuptools import setup

# REQUIRED_PACKAGES = ['tensorflow-gpu==1.6', 'dm-sonnet-gpu']
REQUIRED_PACKAGES = ['tensorflow-gpu==1.6']

setup(
    name='tasks',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='My tasks application package.'
)