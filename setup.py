import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="varclushi-jingtt",
    version="0.0.1",
    author="Xuan Jing",
    author_email="xuanjing@hotmail.com",
    description="A slim package for variable clustering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jingtt/varclushi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
)