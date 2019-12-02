from setuptools import setup, find_packages

setup(
    name="cos_egg",
    version='1.0',
    packages=find_packages(),
    entry_points={'setuptools.installation': ['eggsecutable = src.main.main:main']},
    data_files=[('.', ["__main__.py", 'setup.py', 'requirements.txt'])],
)