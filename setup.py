# -*- coding: utf-8 -*-
import sys
from os.path import join, dirname
from setuptools import setup, find_packages

VERSION = (1, 9, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README'))
long_description = f.read().strip()
f.close()

install_requires = [
    'six',
    'python-dateutil',
    'elasticsearch>=1.0.0,<2.0.0'
]
tests_require = [
    "mock",
    "pytest",
    "pytest-cov",
    "pytz"
]

# use external unittest for 2.6
if sys.version_info[:2] == (2, 6):
    tests_require.append('unittest2')

setup(
    name = "elasticsearch-dsl-legacy",
    description = "Python client for legacy Elasticsearch distribution",
    license="Apache License, Version 2.0",
    url = "https://github.com/PrimerAI/elasticsearch-dsl-py/",
    long_description = long_description,
    version = __versionstr__,
    author = "Rishabh Bhargava",
    author_email = "rishabh@primer.ai", # With a nod to asaplitski, and apologies to honza.kral@gmail.com
    packages=find_packages(
        where='.',
        exclude=('test_elasticsearch_dsl_legacy*', )
    ),
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=install_requires,

    test_suite = "test_elasticsearch_dsl_legacy.run_tests.run_all",
    tests_require=tests_require,
)
