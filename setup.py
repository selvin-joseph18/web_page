from setuptools import setup

setup(
    name='calculator_project_final',
    version='1.0.0',
    packages=['src', 'src.main', 'src.driver', 'test', 'test.main', 'test.driver'],
    url='',
    license='',
    entry_points={'setuptools.installation': ['eggsecutable = src.main.main:main'], },
    data_files=[('.', ['__main__.py'])],
    author='JamunaDeviMurugan',
    author_email='',
    description=''
)