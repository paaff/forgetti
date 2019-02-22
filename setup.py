from setuptools import setup

setup(
    name='forgetti',
    version='0.1.0',
    py_modules=['forgetti'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        forgetti=forgetti:cli
    ''',
)