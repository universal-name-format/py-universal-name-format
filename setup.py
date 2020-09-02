from setuptools import find_packages, setup


with open("README.md", 'r', encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name="unf",
    version="0.1",
    author="k4ng",
    author_email="yh@k4ng.co",
    description="Universal Name Format: JSON-based personal name format utility package",
    long_desription=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/k44ng/universal-name-format",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
