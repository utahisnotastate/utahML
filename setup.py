# [utahML/setup.py]
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="utahML",
    version="1.0.0",
    author="Utah Hans",
    description="The Sovereign AI Operating System. Hyper-spatial computing framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://utahML.io",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9', # Required for advanced AST unparsing
    install_requires=[
        "numpy" # The only dependency. Pure cymatic math.
    ],
)
