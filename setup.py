import subprocess

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

git_version = subprocess.run(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE).stdout.decode(
    'utf-8').strip()

setuptools.setup(
    name="strsimpy",
    version="0.2" + git_version,
    description="A library implementing different string similarity and distance measures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/airenas/python-string-similarity",
    author="ZhouYang Luo, Airenas Vaiciunas",
    author_email="zhouyang.luo@gmail.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[],
    license="MIT License",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
