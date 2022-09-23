import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EasyFileWatcher",                     # This is the name of the package
    version="0.0.4",                        # The initial release version
    # Full name of the author
    author="Efstratios Pahis",
    description="This is yet another FileWatcher. Developed to run smoothier, without sideffects and give more control to the developer in comparison to common packages for such purpose",
    # Long description read from the the readme file
    long_description=long_description,
    long_description_content_type="text/markdown",
    # List of all python modules to be installed
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    license='MIT',
    python_requires='>=3.8',                # Minimum version requirement of the package
    py_modules=["easyfilewatcher"],             # Name of the python package
    # Directory of the source code of the package
    url="https://github.com/efstratios97/EasyFileWatcher",
    install_requires=["apscheduler",
                      "SQLAlchemy",
                      "SQLAlchemy-Utils"]                     # Install other dependencies if any
)
