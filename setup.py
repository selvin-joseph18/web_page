from setuptools import setup,find_packages

setup(
    name='pkg',
    version='1.0.2',
    data_files=[('.',["__main__.py"])],
    entry_points={'setuptools.installation':['pkg = src.main.main:main'], },
    packages=find_packages(exclude=['*tests*']),
)