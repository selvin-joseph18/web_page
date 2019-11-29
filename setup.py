from setuptools import setup, find_packages

setup(

    name='sqtest',
    version='1.0',
    data_files=[('.', ["__main__.py"])],
    entry_points={'setuptools.installation': ['mypackage = src.main.main:main'], },
    packages=find_packages(exclude=['*tests*']),

)
