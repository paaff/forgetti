from setuptools import setup, find_packages

setup(
    name='forgetti',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['forgetti'],
    install_requires=[
        'Click',
    ],
)