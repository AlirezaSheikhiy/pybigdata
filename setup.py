from setuptools import setup, find_packages

with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

setup(
    name="pybigdata",
    version="0.0.1",
    packages=find_packages(),
    description="This python library will eat pigdata.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
)
