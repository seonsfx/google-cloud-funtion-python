#!/usr/bin/env python

# Copyright (C) 2019 SignalFx, Inc. All rights reserved.

from setuptools import setup, find_packages

with open('signalfx_gcf/version.py') as f:
    exec(f.read())

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name=name,  # noqa
    version=version,  # noqa
    author='SignalFx, Inc',
    author_email='info@signalfx.com',
    description='SignalFx GCF Python Wrapper',
    license='Apache Software License v2',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    zip_safe=True,
    packages=find_packages(),
    install_requires=requirements,
    dependency_links=[
        'git+https://github.com/seonsfx/serverless-common-python.git@5a90b53c179a8043487f1a8733434dd3a3c958d3#egg=signalfx_serverless_common'
    ],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    url='https://github.com/seonsfx/google-cloud-funtion-python',
)
