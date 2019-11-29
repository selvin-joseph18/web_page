from setuptools import setup

setup(
    name='factorial_dev',
    version='1.0.1',
    packages=['src', 'src.code', 'src.main', 'test'],
    url='',
    license='',
    data_files=[('.', ["__main__.py"])],
    entry_points={'setuptools.installation':['eggsecutable = src.main.main:main']},
    author='ade.suraj',
    author_email='',
    description=''
)