import setuptools

setuptools.setup(
    name="awesomemodule",
    version="1.0.0",
    description="Tool for printing different hello worlds",
    packages=setuptools.find_packages('src'),
    package_dir={'':'src'}
)