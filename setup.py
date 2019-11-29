from setuptools import setup,find_packages

setup(
    name='ScientificCalculator',
    version='1.0.1',
    packages=find_packages(),
    data_files=[('.', ["__main__.py",'setup.py', 'requirements.txt'])],
    entry_points={'setuptools.installation': ['eggsecutable = src.main.main:main']},

)
