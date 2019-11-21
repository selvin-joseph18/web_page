from setuptools import setup, find_packages

setup(
    name='expfunc_egg',
    version='1.1',
    packages=find_packages(),
    url='',
    entry_points={'setuptools.installation': ['eggsecutable = src.main.main:main'], },
    data_files=[('.', ['__main__.py'])],
    license='',
    author='jayasree.suresh',
    author_email='',
    description=''

)
