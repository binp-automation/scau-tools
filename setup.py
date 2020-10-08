#!/usr/bin/env python3

from setuptools import setup

setup(
    name='scau',
    version='0.0.0',

    description='Scientific automation toolkit',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",

    url='https://github.com/agerasev/scau-tools',

    author='Alexey Gerasev',
    author_email='alexey.gerasev@gmail.com',

    license='MIT',

    py_modules=[name],
    entry_points = {
        'console_scripts': [f'{name}={name}:main'],
    },

    install_requires=open('README.md').read().strip().split('\n'),

    keywords='scientific automation toolkit',
    classifiers=[
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console'
    ]
)
