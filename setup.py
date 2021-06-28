import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Datadistillr",
    version = "1.0",
    author = "Forrest Rogers",
    author_email = "forrest@datadistillr.com",
    description = "Be able to easily use Datadistillr in python",
    long_description = long_description,
    url = "https://github.com/datadistillr/datadistillr-py",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",
    install_requires=[],
    keywords = "datadistillr",
    project_urls={
        "Homepage" : "https://github.com/datadistillr/datadistillr-py"
    },
    entrypoints = {[]},





)