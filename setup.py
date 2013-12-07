from __future__ import unicode_literals

import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-VK',
    version=get_version('mopidy_vk/__init__.py'),
    url='https://github.com/cf8/mopidy-vk',
    license='Apache License, Version 2.0',
    author='cF8',
    author_email='cf8@cf8.ru',
    description='Mopidy extension for VK',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.17',
        'Pykka >= 1.1',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock >= 1.0',
    ],
    entry_points={
        'mopidy.ext': [
            'vk = mopidy_vk:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)