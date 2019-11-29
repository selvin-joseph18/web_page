from setuptools import setup, find_packages

setup(
    name='arithmetic',
    version='1.0',
    data_files=[('.', ["__main__.py"])],
    entry_points={'setuptools.installation': ['pkg = src.main.main:main'], },
    packages=find_packages(exclude=['*tests*']),
)
