"""Setup script for ft_package."""

from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="sedry21",
    author_email="sedry21@42.fr",
    description="A sample test package",
    long_description="A sample test package for learning Python packaging",
    url="https://github.com/sedry21/ft_package",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
