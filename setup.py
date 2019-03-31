import unittest
from setuptools import setup, find_packages
from gendiff.core import __version__


def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='tests.py')
    return test_suite


setup(
   name='gendiff',
   version=__version__,
   description='Compares two configuration files and shows a difference.',
   author='Ivan Dubrovin',
   url='https://github.com/IvanDubrowin/gendiff',
   author_email='ivandubrovin2@mail.ru',
   packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
   package_data={'gendiff': ['*']},
   test_suite='setup.test_suite',
   include_package_data=True,
   )
