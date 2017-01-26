from setuptools import setup

setup(
    name='group',
    version='0.1',
    py_modules=['group'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        group=group:cli
    ''',
)