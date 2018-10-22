import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Application name:
    name="Console Tools",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Brendan T D. Jennings",
    author_email="jbrendan70@outlook.com",

    # Packages
    packages=setuptools.find_packages(),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/MyApplication_v010/",

    #
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "termcolor",
        "colorama",
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)