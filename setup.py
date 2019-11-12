# coding:utf-8

import setuptools


REQUIRES_PYTHON = '>=3.6.0'

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="leetcode_tester",
    version="1.0.4",
    author="Devgum",
    author_email="devgum@foxmail.com",
    python_requires=REQUIRES_PYTHON,
    description="Local tester for Leetcode.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devgum/leetcode_tester",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
