import setuptools

with open("README_EN.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="botank",
    version="0.0.2",
    author="David Dale",
    author_email="dale.david@mail.ru",
    description="A library for automated testing of Alice skills",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avidale/botank",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
)
