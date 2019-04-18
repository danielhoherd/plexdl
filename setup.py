from setuptools import find_packages
from setuptools import setup

dependencies = ["plexapi"]

setup(
    author="Daniel Hoherd",
    author_email="daniel.hoherd@gmail.com",
    include_package_data=True,
    install_requires=dependencies,
    long_description=open("README.md").read(),
    name="plexdl",
    platforms="any",
    version="0.1.0",
    entry_points={"console_scripts": ["plexdl = plexdl.cli:main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: UNLICENSE License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Utilities",
    ],
    packages=find_packages(exclude=("tests*", "testing*")),
)
