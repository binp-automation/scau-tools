#!/usr/bin/env python3

from setuptools import setup

setup(
    name='scau',
    version='0.0.1',

    description='Scientific automation toolkit',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",

    url='https://github.com/agerasev/scau-tools',

    author='Alexey Gerasev',
    author_email='alexey.gerasev@gmail.com',

    license='MIT',

    packages=[''],
    entry_points = {
        'console_scripts': [
            'scau = __main__:main'
        ],
    },

    install_requires=open('requirements.txt').read().strip().split('\n'),

    keywords='scientific automation toolkit',
    classifiers=[
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console'
    ]
)
