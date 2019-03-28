# coding:utf-8

import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="leetcode_tester-Devgum",
    version="1.0.0",
    author="Devgum",
    author_email="devgum@foxmail.com",
    description="Local tester for Leetcode.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devgum/leetcode_tester",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
