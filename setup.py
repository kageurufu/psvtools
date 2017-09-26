#!/usr/bin/env python
# coding: utf-8
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

setup_requires = ['pytest-runner']
install_requires = []
tests_require = ['pytest']

setup(
    name="psvtools",
    version='0.1.0',
    description="Toos for PSV images",
    author="",
    author_email="",
    license="MIT",
    url="https://github.com/kageurufu/psvtrim",
    keywords='PSV trim expand',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "Topic :: System",
        "Topic :: System :: Archiving",
        "Topic :: Utilities"
    ],
    include_package_data=True,
    zip_safe=False,
    setup_requires=setup_requires,
    tests_require=tests_require,
    install_requires=install_requires,
    test_suite="nose.collector",
    entry_points="""\
    [console_scripts]
    psvtools=psvtools.__main__:main
    psvtrim=psvtools.__main__:trim
    psvexpand=psvtools.__main__:expand
    psverify=psvtools.__main__:verify
    """,
)
