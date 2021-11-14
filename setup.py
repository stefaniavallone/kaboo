import os
from setuptools import setup, find_packages


def read_file(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


def read_requirements_file(file_name):
    lines = read_file(file_name).splitlines()
    return [line for line in lines if not line.startswith("--")]


setup(
    name="ktaboo",
    version="0.0.1",
    author="Stefania Avallone",
    author_email="stefaniaavallone3@gmail.com",
    description="",
    package_dir={'ktaboo': 'src/ktaboo'},
    packages=find_packages('src'),
    long_description=read_file('README.md'),
    install_requires=read_requirements_file('requirements.txt'),
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
