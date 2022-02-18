import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="triangle_sector_similarity",
    version="1.2",
    description="Finds similarity between vectors",
    long_description = README,
    long_description_content_type="text/markdown",
    url="https://github.com/mohvam98/triangle-sector-similarity",
    author="mohan98",
    author_email="mohanavamsi98@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["triangle_sector_similarity"],
    include_package_data=True,
    install_requires=['numpy','scipy']
)