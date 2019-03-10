from setuptools import setup

setup(
    name='forgetti',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['forgetti'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        forgetti=forgetti.scripts.forgetti:cli
    ''',
)