import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wsb-analysis", # Replace with your own username
    version="0.0.1",
    author="Vladislav Jidkov",
    author_email="vladjdk@gmail.com",
    description="Data analysis on the most talked about stocks on WSB.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/photonized/wsb-analysis/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)