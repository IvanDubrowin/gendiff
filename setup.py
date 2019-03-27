from setuptools import setup, find_packages
from core import __version__


setup(
   name='gendiff',
   version=__version__,
   description='Compares two configuration files and shows a difference.',
   author='Ivan Dubrovin',
   url='https://github.com/IvanDubrowin/gendiff',
   author_email='ivandubrovin2@mail.ru',
   packages=find_packages()
)
