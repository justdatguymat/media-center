#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='media_center',
    version='1.0',
    description='Media Center',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Matt Koltun',
    author_email='matt@koltunm.com',
    url='https://github.com/justdatguymat/media-center',
    package_dir={
        "" : "src"
    },
    packages=find_packages(where="./src"),
    entry_points={
        'console_scripts': [
            'media-center-start=media_center.main:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
