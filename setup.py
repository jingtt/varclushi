import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="varclushi",
    version="0.0.7",
    author="Xuan Jing",
    author_email="xuanjing@hotmail.com",
    description="A package for variable clustering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jingtt/varclushi",
    packages=setuptools.find_packages(),
	install_requires=[
		"pandas",
		"numpy",
		"factor-analyzer",
	],
    classifiers=[
		"Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
		"Operating System :: Microsoft :: Windows",
		"Operating System :: POSIX :: Linux",
		"Operating System :: Unix",
    ],
)
