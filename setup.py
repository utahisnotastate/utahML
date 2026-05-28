from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="utahml",
    version="1.1.0",
    author="Utah Hans",
    description="The Sovereign AI Operating System. Hyper-spatial computing framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/utahisnotastate/utahML",
    project_urls={
        "Repository": "https://github.com/utahisnotastate/utahML",
        "Issues": "https://github.com/utahisnotastate/utahML/issues",
        "Documentation": "https://github.com/utahisnotastate/utahML/tree/main/docs",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "torch",
        "opencv-python",
        "watchdog",
    ],
)
