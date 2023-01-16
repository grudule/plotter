from setuptools import setup, find_packages

setup(
    name="pre_gpumcd",
    version="1.1.0",
    author="grudule",
    author_email="alexandre.sagona.1@ulaval.ca",
    description="Plotting easily",
    url="https://github.com/grudule/plotter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy~=1.23.0",
    ]
)
