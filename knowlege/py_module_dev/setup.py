from setuptools import setup, find_packages
setup(
    name = "mypackage",
    version = "1.0",
    author = "Xinlong Li",
    packages = find_packages(),
    package_data = {"mypackage":["me.py","print_xinlong.py"]}
)
