from setuptools import setup

setup(
    name='django-hierarchical-auth',
    version='0.4',
    author='Stefano Crosta (scrosta)',
    original_author='Ivan Raskovsky (rasca)',
    author_email='stefano@digitalemagine.com',
    original_author_email='raskovsky@gmail.com',
    packages=['hierarchical_auth',],
    # license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Extends django auth allowing hierarchical permissions',
    long_description=open('README.rst').read(),
)
