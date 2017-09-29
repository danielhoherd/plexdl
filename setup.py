# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup

dependencies = ['click', 'plexapi']

setup(
    name='plexdl',
    version='1.0.0',
    author='Daniel Hoherd',
    author_email='daniel.hoherd@gmail.com',
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'plexdl = plexdl.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=('tests*', 'testing*')),
)
