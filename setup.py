from setuptools import setup

setup(
    name='10_power_x',
    version='1.0',
    packages=['src', 'src.main', 'src.driver', 'test', 'test.main', 'test.driver'],
    entry_points={'setuptools.installation': ['eggsecutable = src.main.main:main'], },
    data_files=[('.', ['__main__.py'])],
    author='JamunaDeviMurugan',
)