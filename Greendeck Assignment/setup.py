import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Greendeck-ukanhaupa",
    version="0.0.1",
    author="Kanha Upadhyay",
    author_email="mr.kanhaupadhyay@gmail.com",
    description="greendeck assignment package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ukanhaupa/Greendeck",
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: NA :: NA",
        "Operating System :: OS Independent"
        ],
    python_requires='>=3.6',
)
