from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in demo_order_app/__init__.py
from demo_order_app import __version__ as version

setup(
	name="demo_order_app",
	version=version,
	description="Demo Frappe Application for Taking Orders",
	author="jeomar bayoguina",
	author_email="jeomar.bayoguina@ghd.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
